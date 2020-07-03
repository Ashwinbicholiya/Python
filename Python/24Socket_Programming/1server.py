import socket

s = socket.socket()
print('Socket created')

s.bind(('localhost',9999))
s.listen(3)  #3 clent waiting for connection 
print('Waiting for connections')

while True: 
    c , addr = s.accept()
    print('Connected with', addr)

    c.send('Welcome to Telusko')

    c.close()