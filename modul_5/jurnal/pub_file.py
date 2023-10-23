# import mqtt library
import paho.mqtt.client as mqqt
# import base64 untuk decode dan encode
import base64

# import library time supaya bisa menggunakan sleep
import time
# tentukan broker yang digunakan (Hint: test.mosquitto.org port 1883)
address = "test.mosquitto.org"
# tentukan port yang digunakan
port = 1883
# buat client
client = mqqt.Client()


# baca file kemudian encode file tersebut menggunakan base64
with open("data.jpg", "rb") as f:
    isi_file = f.read()

# variabel "hasil_konversi_ke_base64" akan dikirimkan sebagai pesan
hasil_konversi_ke_base64 = base64.b64encode(isi_file)

# koneksi ke broker
client.connect(address, port)
# publisher mulai


# publish message
result = client.publish("photo_topic_file_1304211035",
                        hasil_konversi_ke_base64, qos=0)

# cek jika message berhasil dipublish atau tidak
if result[0] == 0:
    print("publish berhasil")
else:
    print("publish tidak berhasil")


# end publish
