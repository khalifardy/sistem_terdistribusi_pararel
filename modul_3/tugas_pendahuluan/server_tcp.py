import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024
clients = []


def send_message(client_socket, message):
    for client in clients:
        if client in clients:
            if client != client_socket:
                try:
                    client.send(message)
                except Exception as _:
                    remove_client(client)


def remove_client(client):
    if client in clients:
        clients.remove(client)


def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(BUFFER_SIZE)
            if not message:
                break
            send_message(client_socket, message)
    except Exception as e:
        print(str(e))
    finally:
        client_socket.close()
        remove_client(client_socket)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)
print("start server")
while True:
    conn, addr = s.accept()
    clients.append(conn)
    print("Alamat: ", addr)
    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()
