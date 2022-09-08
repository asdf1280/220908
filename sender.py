# broadcast "hello world" to udp port 12345

import socket

# ask name to console
name = input("Enter your name: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    message = input("메시지 입력 > ")
    if message == "exit":
        break

    # send message to server
    ba = bytearray()
    data = name.encode("utf-16")
    ba.extend(len(data).to_bytes(4, byteorder='big'))
    ba.extend(data)
    data = message.encode("utf-16")
    ba.extend(len(data).to_bytes(4, byteorder='big'))
    ba.extend(data)

    print(ba)

    sock.sendto(ba, ('255.255.255.255', 64345))