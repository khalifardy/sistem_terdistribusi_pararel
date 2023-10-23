# import time
import time

# import library mqtt yang digunakan
import paho.mqtt.client as mqqt

# import base64 untuk encode dan decode file
# file pdf, jpg merupakan file berbentuk binary. tidak bisa langsung mengirim format biner harus diubah menjadi bentuk yang sesuai
import base64
import io


# tentukan alamat broker yang digunakan
address = "test.mosquitto.org"

# tentukan port yang digunakan oleh broker  (Hint: test.mosquitto.org port 1883)
port = 1883

# buat client
client = mqqt.Client()

# koneksi ke brokeer
client.connect(address, port)

# buat callback pada saat menerima pesan dan menulis/menyimpan file tersebut


def on_message(cln, obj, msg):

    data = msg.payload.decode()
    msg = str(data)
    img = msg.encode('ascii')
    binary_data = base64.b64decode(img)
    with open("data_gambar.jpg", "wb") as f:
        f.write(binary_data)

    # tulis hasil file yang didapat
    # jangan lupa melakukan decode img menggunakan based64


# buat callback pada saat client berhasil subscribe
def on_subscribe(client, userdata, mid, granted_qos):
    print("Berhasil Subscribe")


# lakukan subscribe sesuai topik yang dipilih
client.subscribe("photo_topic_file_1304211035")


# panggil callback saat subscribe
client.on_subscribe = on_subscribe

# subscriber siap menerima
client.on_message = on_message

time.sleep(5)
client.loop_forever()
