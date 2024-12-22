import paho.mqtt.client as mqtt
import time

# Configuración del broker MQTT
BROKER = "mqtt.eclipseprojects.io"
PORT = 1883
TOPIC = "smartterrarium/data"

# Crear cliente MQTT
client = mqtt.Client()

# Conectar al broker
client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        # Crear un mensaje de ejemplo
        message = {
            "temperature": 25.5,
            "humidity": 60.2,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        client.publish(TOPIC, str(message))
        print(f"Publicado: {message}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Finalizando...")
finally:
    client.loop_stop()
    client.disconnect()
