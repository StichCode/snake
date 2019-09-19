import json
import socket

from data import from_send


def create_host(port, clients):
    sock = socket.socket()
    sock.bind(('', port))
    sock.listen(clients)
    print("Waiting for connection player...")
    conn, addr = sock.accept()
    print("Player is connect")
    return sock, conn, addr


def getting_data(sock, conn, addr):
    data = conn.recv(100000)
    print(from_send(data))
    conn.send(data.upper())

    print("Player is disconnect")


sock, conn, addr = create_host(9090, 3)
getting_data(sock, conn, addr)

# TODO: Метод десиарилизации и сирриализации входных и выходных данных
# TODO: Метод отправки и получения данных
# TODO: Сделать эти методы общими для клиента и сервера
