import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 8888))
time = server.recv(1024)
client.send(input("///"))
server.close()
print("Текущее время: %s" % tm.decode('ascii'))
