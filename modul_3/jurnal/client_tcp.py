import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('localhost', 3000)

client.connect(server_addr)

file_name = input("masukan nama file: ")
# client.send(file_name.encode())

with open(file_name, 'rb') as file:
    # byte = file.read(1)
    while True:
        byte = file.read(1)
        if byte == b'':
            break
        client.send(byte)

print("selesai mengirim file")
