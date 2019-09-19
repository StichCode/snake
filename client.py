# -*- coding: utf-8 -*-
import json
import socket

from data import to_send

ol = {
    "id": 1,
    "name": "petya",
    "pos": (1, 10)
}


def create_connect(ip, port):
    sock = socket.socket()
    sock.connect((ip, port))
    return sock


def send_data(sock, data):
    sock.send(to_send(data))
    data = sock.recv(100000)
    print(data.decode("utf-8"))


send_data(create_connect("localhost", 9090), ol)
