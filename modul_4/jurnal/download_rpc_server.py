# import library SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# import xmlrpc bagian client
from xmlrpc.client import Binary


# buatlah fungsi pada server yang bernama download()
def file_download():

    # buka file bernama "file_server_didownload.txt"
    try:
        with open("file_server_download.txt", 'rb') as handle:
            file = handle.read()
            # kirimkan file tersebut dalam bentuk xml dengan cara memanggil xmlrpc.client.Binary()
            return Binary(file)
    except FileNotFoundError:
        return "File tidak ditemukan"


# buat server pada IP dan port yang telah ditentukan
ip = 'localhost'
port = 8008
server = SimpleXMLRPCServer((ip, port))

# print bahwa "server mendengarkan pada port xxx"
print("Listening on port 8008")

# register fungsi download pada server
server.register_function(file_download, "download")

# jalankan server
server.serve_forever()
