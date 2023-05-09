import paho.mqtt.client as mqtt
import time
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")

broker_hostname = "localhost"
port = 1883


def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", return_code)


client = mqtt.Client("andrea")
client.username_pw_set(username, password)
client.on_connect = on_connect

client.connect(broker_hostname, port)
client.loop_start()

topic = "general"
msg_count = 0

try:
    for i in range(10):
        time.sleep(1)
        msg = "Message " + str(msg_count)
        client.publish(topic, msg)
        print("Published message: " + msg)
        msg_count += 1
finally:
    client.loop_stop()
