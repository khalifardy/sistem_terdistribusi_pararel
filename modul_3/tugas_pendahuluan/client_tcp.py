import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024


def receive_message(client):
    while True:
        data = client.recv(BUFFER_SIZE)
        if data:
            print(" ")
            print("pesan diterima client 2: ", data.decode())


s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

receive_thread = threading.Thread(target=receive_message, args=(s,))
receive_thread.start()

while True:
    pesan = input("silahkan tulis pesan client 1: ")
    s.send(pesan.encode())
    if pesan == "quit":
        break
    resp = s.recv(BUFFER_SIZE)
    if resp:
        print("pesan diterima client 2: ", resp.decode())

s.close()
