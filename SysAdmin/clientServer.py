import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1',1234))

s.listen(3)

c,address = s.accept()

print('connection recieved from {} '.format(address))

banner = 'Hi, this is Server!'
c.send(banner.encode())

c.close()

s.close()