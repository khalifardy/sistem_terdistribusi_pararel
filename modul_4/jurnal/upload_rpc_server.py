# import SimpleXMLRPCServer bagian server
from xmlrpc.server import SimpleXMLRPCServer

# buat fungsi bernama file_upload()


def file_upload(filedata):

    # buka file
    with open("hasil_upload.txt", 'wb') as handle:
        # konversi supaya dapat ditulis IMPORTANT!
        data1 = filedata.data

        # tulis file tersebut
        handle.write(data1)
        return True  # IMPORTANT


# buat server
ip = 'localhost'
port = 8008
server = SimpleXMLRPCServer((ip, port))

# tulis pesan server telah berjalan
print("Listening on port 8008")

# register fungsi
server.register_function(file_upload, "upload")

# jalankan server
server.serve_forever()
