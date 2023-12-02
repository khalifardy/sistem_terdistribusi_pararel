import os  # import library os
import re  # import library re
import datetime  # import library datetime
import threading  # import library threading
import time  # import library time

# compile regex dengan regex pattern == 'Sent = (\d)' untuk pengirim dan 'Received = (\d)' untuk penerima,
# regex filter ini akan digunakan untuk mencari bilangan bulat x dalam suatu string 'Sent = x' 'dan Received = y'
regex_sent_filter = re.compile('(\d) paket dikirim')
regex_received_filter = re.compile('(\d) diterima')


class ip_check(threading.Thread):

    # inisialisasi thread
    def __init__(self, IP):
        super().__init__(target=self.run())
        self.IP = IP   # inisialisasi IP
        self.status_pengirim = -1  # inisialisasi status dengan '-1'
        self.status_penerima = -2  # inisialisasi status dengan '-2'

    # fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):

        # lakukan ping sebanyak 2 kali kepada alamat IP penerima
        ping_output = os.popen(f'ping -c 2 {IP}')

        while True:  # loop forever

            # baca luaran dari command ping tiap baris
            baris = ping_output.readline()

            if not baris:
                break  # akan keluar dari loop jika tidak ada lagi baris

            # lakukan filtering dengan regex, gunakan method findall()
            # pada regex filter yang sudah di-inisialisasi sebelumnya
            status_pengirim = regex_sent_filter.findall(baris)
            status_penerima = regex_received_filter.findall(baris)

            # set atribut status_pengirim dan status_penerima
            if (status_penerima and status_pengirim):
                self.status_pengirim = status_pengirim[0]
                self.status_penerima = status_penerima[0]


# status alamat IP pengirim
sent_status = {
    '0': 'PENGIRIMAN GAGAL',
    '1': 'TERKIRIM NAMUN TIDAK SEMUA',
    '2': 'TERKIRIM'
}

# status alamat IP penerima
ip_status = {
    '0': 'TIDAK ADA RESPON',
    '1': 'HIDUP NAMUN ADA PAKET YANG HILANG',
    '2': 'HIDUP'
}

workers = []  # buat list untuk menampung hasil pengecekan

# inisalisasi 15 IP berbeda dengan salah satu IP merupakan IP local
IPs = [
    'localhost', 'google.com', 'milan.id.domainesia.com', 'symbolic.id', 'instagram.com',
    'symbolic.id', 'youtube.com', 'caknun.com', 'kompas.com', 'gramedia.com',
    'mojok.co', 'frisidea.com', 'telkomuniversity.ac.id', 'langitselatan.com', 'itb.ac.id'
]

# ambil waktu awal menggunakan method datetime.now() dari library datetime
waktu_awal = datetime.datetime.now()
i = 1

# lakukan ping ke-15 alamat tersebut
for IP in IPs:

    worker = ip_check(IP)    # inisialisasi thread untuk setiap IP
    workers.append(worker)             # masukkan setiap thread dalam list
    worker.start()             # jalankan thread

for worker in workers:

    worker.join()  # tunggu hingga seluruh thread selesai

    # tampilkan hasilnya
    print(f'{i}.\tPinging {worker.IP}\t ,',
          f' Status pengirim = {sent_status[worker.status_pengirim]},',
          f'\t Status penerima ={ip_status[worker.status_penerima]}')
    i += 1

# ambil waktu akhir menggunakan method datetime.now() dari library datetime
waktu_akhir = datetime.datetime.now()

# tampilkan waktu awal dan waktu akhir eksekusi
print(f'\nWaktu awal = {waktu_awal}, Waktu akhir = {waktu_akhir}')

# tampilkan selisih waktu akhir dengan waktu awal untuk mengetahui lama waktu eksekusi.
# catatan: gunakan method timestamp() dari waktu_awal dan waktu_akhir untuk menghitung selisih
print(f'Lama waktu eksekusi = {waktu_akhir.timestamp()-waktu_awal.timestamp():.2f}',
      'detik')

# gunakan delay dengan Library time untuk mencegah fast close dengan isi parameter 40
time.sleep(40)
