import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создает сокет TCP
server.bind(('', 8888)) # ссылаемся на localhost и присваивание порта
server.listen(5)# переходит в режим прослушки
           # не более 5 запросов


while True:
    client, addr = server.accept()
    print("Yor status is online".encode(UTG-8) % str(addr))
    timestr = time.ctime(time.time()) + '\n'
    client.send(timestr.encode('ascii'))
    data = user_socket.recv(1024)
    client.close()


