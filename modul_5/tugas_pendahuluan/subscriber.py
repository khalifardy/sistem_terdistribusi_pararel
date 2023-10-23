import paho.mqtt.client as mqtt


def pesan(client, userdata, message):
    print(f'waktu publisher: {message.payload.decode()}')


client = mqtt.Client()

client.on_message = pesan

client.connect("localhost", 1883)

topic = "info_waktu"
client.subscribe(topic)
client.loop_forever()
