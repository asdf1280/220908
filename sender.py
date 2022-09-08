# broadcast "hello world" to udp port 12345

import socket

# ask name to console
name = input("Enter your name: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    message = input("> ")
    if message == "exit":
        break

    # send message to server
    ba = bytearray()
    ba.extend(len(name).to_bytes(4, byteorder='big'))
    ba.extend(name.encode("utf-8"))
    ba.extend(len(message).to_bytes(4, byteorder='big'))
    ba.extend(message.encode("utf-8"))

    sock.sendto(ba, ('255.255.255.255', 12345))