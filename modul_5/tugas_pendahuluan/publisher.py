import paho.mqtt.client as mqtt
import time
import datetime

# insialisasi client MQQT
client = mqtt.Client()

# koneksikan ke broker MQQT
client.connect("localhost", 1883)

# publish pesan ke topik tertentu
print("start publisher")
while True:
    topic = "info_waktu"
    pesan = datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")
    client.publish(topic, pesan)
    time.sleep(10)

# client.disconnect()
