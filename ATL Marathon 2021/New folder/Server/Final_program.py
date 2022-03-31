from random import randint
import socket
from time import sleep

HOST, PORT = "localhost", 9999

while True:
    
    # Code to calculate values here start

    id_num = 1
    averageBodyTemp = randint(0,40)
    bp = randint(100,140)
    hb = randint(0,100)
    spo2 = randint(0,100)

    # Code to calculate values here end

    data = '-'.join((str(id_num), str(bp), str(hb), str(averageBodyTemp), str(spo2)))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
    print('Sent:' + data)
    sleep(10)