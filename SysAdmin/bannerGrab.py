import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.0.72', 22))

msg = s.recv(2048).decode()

print(msg)

s.close()