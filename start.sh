#!/bin/bash
# Inicia la aplicación Flask en segundo plano
python app.py &

# Inicia el script MQTT
python mqtt_publisher.py
