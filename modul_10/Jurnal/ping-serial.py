import os  # import library os
import re  # import library re
import datetime  # import library datetime
import time  # import library time

# compile regex dengan regex pattern == 'Sent = (\d)' untuk pengirim dan 'Received = (\d)' untuk penerima,
# regex filter ini akan digunakan untuk mencari bilangan bulat x dalam suatu string 'Sent = x' 'dan Received = y'
regex_sent_filter = re.compile('(\d) paket dikirim')
regex_received_filter = re.compile('(\d) diterima')


"""
READ ME

Contoh luaran command ping yang berhasil dengan CMD
Command CMD: ping 192.168.10.1 -n 2 (lakukan ping ke alamat IP 192.168.10.1 sebanyak 2 kali)

Pinging 192.168.10.1 with 32 bytes of data:
Reply from 192.168.10.1: bytes=32 time<1ms TTL=128
Reply from 192.168.10.1: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.10.1:
    Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Terlihat pada bagian Ping statistics bahwa paket dikirim dan diterima sebanyak 2 kali,
artinya seluruh paket berhasil diterima oleh alamat IP 192.168.10.1.

Dengan ini dapat dikatakan bahwa angka received dan sent dapat menyatakan
kondisi alamat IP 192.168.10.1 dengan detail sebagai berikut:
- Received = 0 (tidak ada paket yang diterima, TIDAK ADA RESPON)
- Received = 1 (ada paket yang diterima, HIDUP NAMUN ADA PAKET YANG HILANG)
- Received = 2 (seluruh paket diterima, HIDUP)

- Sent = 0 (paket gagal dikirim, PENGIRIMAN GAGAL)
- Sent = 1 (Paket berhasil dikirim namun tidak semua, TERKIRIM NAMUN TIDAK SEMUA)
- Sent = 2 (paket berhasil dikirim, TERKIRIM)

Yang akan dicari dengan regex 'Sent = (\d)' dan 'Receiver = (\d)' adalah status tersebut (0, 1, atau 2).
"""

# status alamat IP pengirim berdasarkan penjelasan diatas
sent_status = {
    '0': 'PENGIRIMAN GAGAL',
    '1': 'TERKIRIM NAMUN TIDAK SEMUA',
    '2': 'TERKIRIM'
}

# status alamat IP penerima berdasarkan penjelasan diatas
ip_status = {
    '0': 'TIDAK ADA RESPON',
    '1': 'HIDUP NAMUN ADA PAKET YANG HILANG',
    '2': 'HIDUP'
}

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

    # lakukan ping sebanyak 2 kali kepada alamat IP penerima
    print(IP)
    print(f'{i}.\t Pinging {IP} \t', end='')
    i += 1
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

        # tampilkan status IP pengirim dan penerima apabila filter menemukan string yang cocok
        if (status_penerima and status_pengirim):
            print(f'\t Status_pengirim = {sent_status[status_pengirim[0]]},'
                  f'\t Status_penerima={ip_status[status_penerima[0]]}')

        print("")

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
