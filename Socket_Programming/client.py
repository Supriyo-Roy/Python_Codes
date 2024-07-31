import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
s.connect((host,1234))
msg=s.recv(1028)
print("Message receievd from server"+msg.decode("utf-8"))