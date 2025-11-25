# Step to link ThingsBoard and and the captors

_(Doc :)[https://thingsboard.io/docs/reference/]_

After executing this command you can open http://{your-host-ip}:8080 in you browser (for ex. http://localhost:8080). You should see ThingsBoard login page. Use the following default credentials:

* System Administrator: sysadmin@thingsboard.org / sysadmin
* Tenant Administrator: tenant@thingsboard.org / tenant
* Customer User: customer@thingsboard.org / customer

You can always change passwords for each account in account profile page.

You can safely detach from the log stream (e.g. Ctrl+C); containers will continue running. 
_from (ThingsBoard user guide)[https://thingsboard.io/docs/user-guide/install/docker/]_

```shell
sudo docker compose run --rm -e INSTALL_TB=true -e LOAD_DEMO=true thingsboard-ce

docker compose up -d && docker compose logs -f thingsboard-ce
```

Connect with the tnnant to add a device.

Give it a name.

Next step, select MQTT.

Take the API key in the exemple commande, paste it in the python file.

Voila.