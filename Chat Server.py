import socket
from threading import Thread
import random

def accept_incoming_connections():
    while True:
        client, client_adress = SERVER.accept()
        client.send("Your messages are secured by encryption. Choose a nickname for yourself.".encode())
        print("%s:%s has connected" % client_adress)
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(1024).decode()
    welcome = 'Welcome %s! If you ever want to quit, type {EXIT} to exit.' % name
    client.send(bytes(welcome, "utf8"))

    #Make sure that every client has a distinct id
    while 1:
        client_id=random.randint(0,100)
        if client_id not in list(clients.values()):
            clients[client]=client_id
            break
        else:
            continue


    #Make sure that every client has a distinct peer

    if len(clients)>=3:
        while 1:
            target_client=random.choice(list(clients.values()))
            if target_client not in list(match.keys()) or list(match.values()):
                match[client_id]=target_client
                break
            else:
                continue




    print(clients.values())
    print(match)

    while True:
        msg=client.recv(1024)
        frm=clients[client]
        try:
            to=match[frm]
        except KeyError:
            to=list(match.keys())[list(match.values()).index(frm)]

        to_client=list(clients.keys())[list(clients.values()).index(to)]
        to_client.send(msg)





clients={}
match={}




HOST = "0.0.0.0"
PORT = 5000
ADDR = (HOST,PORT)

SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SERVER.bind(ADDR)

if __name__== "__main__":
    SERVER.listen(5)
    print("Waiting for connection.....")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()