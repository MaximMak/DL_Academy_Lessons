import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создает сокет TCP
s.bind(('', 8888)) # присваивание поорта
s.listen(5)# переходит в режим прослушки
           # не более 5 запросов


while True:
    client, addr = s.accept()
    print("Get acsses to conection from %s" % str(addr))
    timestr = time.ctime(time.time()) + '\n'
    client.send(timestr.encode('ascii'))
    client.close()


