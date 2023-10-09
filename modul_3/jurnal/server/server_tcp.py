import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 3000)
server.bind(address)

server.listen(1)
print("menunggu koneksi dari klien")

client, addr = server.accept()
print("terhubung dengan: ", addr)

# file = client.recv(1024).decode()

with open("results.txt", 'wb') as files:
    while True:
        data = client.recv(1024)
        if not data:
            break
        files.write(data)

print("FIle berhasil disimpan")
client.close()
server.close()
