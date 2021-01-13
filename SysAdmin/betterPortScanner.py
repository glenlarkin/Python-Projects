import socket




ports = input('Enter range of ports like 1-1000 :\n')


start,end = ports.split('-')
start = int(start)
end = int(end)

for i in range(start,end+1):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('192.168.0.72', i))
        print('port '+ i + ' is opened')
        s.close()

    except:
        pass
    #print('port {} is closed'.format(i))
