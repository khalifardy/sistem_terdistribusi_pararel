# import xmlrpc bagian client
import xmlrpc.client

# buat proxy untuk mengakses server. Gunakan parameter URL server yang akan diakses berupa IP dan port. Bentuk http://IP:port
url = 'http://localhost:8008'
s = xmlrpc.client.ServerProxy('%s' % url)

# buat file baru dengan pada client denga nama "file_hasil_download.txt" sebagai hasil download dari server
with open("file_hasil_download.txt", "wb") as handle:
    file = s.download().data
    # tulis/isi file hasil_download.txt dengan hasil dari memanggil fungsi "download" yang berada server
    handle.write(file)
    # jangan lupa untuk mengubah/konversi file menjadi binary dengan menambahkan .data


print("file berhasil di download")
