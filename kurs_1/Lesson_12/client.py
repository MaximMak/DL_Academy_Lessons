import socket, threading, time, logging


logging.basicConfig(
    filename="app.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.info
)


shutdown = False
join = False


def reciving(aliase, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
unic_id = 0
server = ("127.0.0.1", 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создает сокет TCP
s.setblocking(0)

alias = input('Input your name for chat: ')

rT = threading.Thread(target=reciving, arg=("RecvThread", s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("[" + alias + "] => join chat, status online ").encode("UTF-8"), server)
        join = True
    else:
        try:
            message = input("Input your message: ")
            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("UTF-8"), server)
                time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= Left the chat, status offline ").encode("UTF-8"), server)
            shutdown = True


rT.join()
s.close()
