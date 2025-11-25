import random
import time
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
KEY = "CQl7gttGyfhBrX8W2tC6"

state = {
    "temperature": 24.0,
    "humidity_air": 60.0,
    "soil_moisture": 45.0,
    "co2": 500,
    "oxygen": 209000,
    "luminosity": 30000,
    "pump_state": False,
    "fan_state": False,
    "light_state": False
}

def simulate_step():
    state["temperature"] += random.uniform(-0.2, 0.2)
    state["humidity_air"] += random.uniform(-0.5, 0.5)

    if state["pump_state"]:
        state["soil_moisture"] += random.uniform(0.5, 1.0)
    else:
        state["soil_moisture"] += random.uniform(-0.3, -0.1)

    state["co2"] += random.uniform(-2, 2)
    state["luminosity"] += random.uniform(-500, 500)

    state["temperature"] = max(10, min(40, state["temperature"]))
    state["humidity_air"] = max(20, min(90, state["humidity_air"]))
    state["soil_moisture"] = max(0, min(100, state["soil_moisture"]))
    state["co2"] = max(300, min(2000, state["co2"]))
    state["luminosity"] = max(0, min(80000, state["luminosity"]))

    state["oxygen"] += random.uniform(-0.02, 0.02)
    state["oxygen"] = max(19.0, min(21.0, state["oxygen"]))

def on_connect(client, userdata, flags, rc):
    print("Connected to brocker :", rc)

def on_message(client, userdata, message):
    global state
    payload = message.payload.decode()
    try:
        cmd = json.loads(payload)
        for key, value in cmd.items():
            if key in state:
                state[key] = value
                print(f"Actionneur {key} mis à : {value}")
    except:
        print("Unknown reception")

def main():
    client = mqtt.Client()
    client.username_pw_set(username=KEY, password="")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    client.subscribe("v1/devices/me/rpc/request/+")

    client.loop_start()

    print("Simulation...")

    try:
        while True:
            simulate_step()
            payload = json.dumps(state)
            client.publish("v1/devices/me/telemetry", payload)
            print("Pubblished data :", payload)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stop")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
