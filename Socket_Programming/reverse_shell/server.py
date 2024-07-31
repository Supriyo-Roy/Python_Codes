import socket
import sys ##is used to issue commands in cli

# create a socket
def create_socket():
    try:
        global host 
        global port
        global s
        host=""
        port=9999
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket creation error " +str(msg))    
        
def bind_socket():
    try:
        global host 
        global port
        global s
        print(f"Binding port: {port}")
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(f"Socket binding error {msg}")
        print("Retrying........")
        bind_socket() #Recursion(Function calling itself)
        
def socket_accept():
    conn,addr=s.accept()
    print("Connection Established!!!!! ip address = {addr[0]} and the port {addr[1]}")
    send_commands(conn)
    s.close()
    
#send command   
def send_commands(conn):
    #we are using infinite loop because lets say we issued a command , after that got executed the connection will close, but we want to keep it persisted
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit() #this will close our command prompt
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"utf-8")   #converting to string as we recieve data in byte format
            print(client_response,end="") #end="" to go the next line
            
def main():
    create_socket()
    bind_socket()
    socket_accept()            
    
main()    
        
            
            