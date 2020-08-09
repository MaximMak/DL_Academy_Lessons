import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))
tm = s.recv(1024)
s.close()
print("Текущее время: %s" % tm.decode('ascii'))
