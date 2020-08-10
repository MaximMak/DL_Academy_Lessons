import socket
import time


host = socket.gethostbyname(socket.gethostname())
port = 8888

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создает сокет TCP
s.bin((host, port))

quit = False
print("Server started")

while not quit:
    try:
        data, unic_id = s.recvfrom(1024)
        if unic_id not in clients:
            clients.append(unic_id)
            inst_time = time.strftime('%H.%M.%S', time.localtime())
            print("["+unic_id[0]+"]=["+str(unic_id[1])+"]=["+inst_time+"]/", end="")
            print(data.decode("utf-8"))
            for client in clients:
                if unic_id != client:
                    s.sendto(data, client)
    except:
        print("\n [ Server Stopped!]")
        quit = True

s.close()