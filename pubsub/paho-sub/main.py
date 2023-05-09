import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("general")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect("localhost", 1883)
client.loop_forever()
