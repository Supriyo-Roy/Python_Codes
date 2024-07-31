import socket

# create a socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
s.bind((host,1234))

#The listen method enables the server to accept connections. The 5 specifies the maximum number of queued connections.
s.listen(5)

while True:
    conn,addr=s.accept()
    print(f"Connected to {addr}")
    conn.send(bytes("Socket Programing in Python","UTF-8"))