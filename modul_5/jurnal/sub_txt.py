# Import library time
import time
# Import library MQTT
import paho.mqtt.client as mqqt
# Tentukan broker yang digunakan (Hint: test.mosquitto.org port 1883)
address = "test.mosquitto.org"
# Tentukan port yang digunakan
port = 1883
# Buat client
client = mqqt.Client()
# Koneksikan client
client.connect(address, port)


def on_message(mosq, obj, msg):
    print("Ada pesan")
    # print(msg.payload.decode("utf-8"))
    with open('pesan.txt', 'w') as fd:
        fd.write(msg.payload.decode("utf-8"))


# Buat callback saat berhasil subscribe
def on_subscribe(client, userdata, mid, granted_qos):
    print("Berhasil Subscribe")


# Lakukan subscribe
result = client.subscribe("photo_topic_1304211035", 0)
print(result)

# Panggil callback on_subscribe untuk client
client.on_subscribe = on_subscribe
print("Subscribing...")

# Panggil callback on_message untuk client
client.on_message = on_message
# Mulai loop client

# Berikan delay (sleep) 4
time.sleep(4)
client.loop_forever()
