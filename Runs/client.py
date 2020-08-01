import socket
from Game.Messages import StartGameMessage

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    s.send(b"ack")

    data = StartGameMessage().decode(data).array[0]

    if data == "Q":
        print("The Game Break")
        break

    elif data == "I":
        inp_1 = s.recv(1024)
        inp_1 = StartGameMessage().decode(inp_1).array[0]
        inp = input(inp_1)
        StartGameMessag = StartGameMessage(inp)
        s.sendall(StartGameMessag.encode())

    else:
        print(data)

s.close()
