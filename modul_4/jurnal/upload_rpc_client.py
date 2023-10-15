# import xmlrpc bagian client
import xmlrpc.client
from xmlrpc.client import Binary
# buat stub proxy client
url = 'http://localhost:8008'
s = xmlrpc.client.ServerProxy('%s' % url)

# buka file yang akan diupload
with open("file_diupload.txt", 'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    file = Binary(handle.read())

# panggil fungsi untuk upload yang ada di server
    result = s.upload(file)

if result:
    print("file berhasil di upload")
else:
    print("file gagal di upload")
