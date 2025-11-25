# Dashboard Greenhouse

Équipe : Charrier Titouan, Fourré Simon

## Principe général

Notre projet consiste à créer un dashboard pour la gestion et le suivi en temps réel d’une serre. L’objectif est de visualiser les données environnementales et de piloter les équipements de manière intuitive.
Fonctionnalités prévues

- Visualisation 3D ou carte de la serre : pour situer les capteurs et zones de culture

- Données temps réel : température, humidité, luminosité, CO₂ via Mosquitto MQTT et ThingsBoard

- Graphiques et statistiques : suivi de l’évolution des paramètres avec Chart.js

- Filtres interactifs : trier les relevés par zone, date ou type de plante

- Alertes et notifications : seuils critiques pour température ou humidité

- Exploration avancée : cliquer sur un capteur pour voir l’historique ou détails

## Sources

    Capteurs IoT connectés via MQTT, intégrés à ThingsBoard pour la collecte et la visualisation des données

