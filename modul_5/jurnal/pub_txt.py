# Import MQTT Client
import paho.mqtt.client as mqqt
import time
# Buat broker address
address = "test.mosquitto.org"
# Tentukan port yang akan digunakan (Hint: test.mosquitto.org port 1883)
port = 1883
# Buat client
client = mqqt.Client()
# Koneksikan ke broker dan port
client.connect(address, port)
# Baca file
while True:
    f = open("data.txt")
    string_data = f.read()
    arraybytr = string_data.encode()
    # Publish
    topic = "photo_topic_1304211035"
    result = client.publish(topic, arraybytr)

    # Cek jika message berhasil dipublish atau tidak
    if result[0] == 0:
        print("Berhasil publish")
    else:
        print("tidak berhasil publish")
    time.sleep(5)
