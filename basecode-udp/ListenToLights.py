#!/usr/bin/env python3

import socket
from builtins import bytes


UDP_IP = "172.18.0.1"
UDP_PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
    data = data.decode()
        if data[0]:
            print("Received message: {}".format(data))

