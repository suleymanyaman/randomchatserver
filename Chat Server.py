import socket
from threading import Thread
import random

def accept_incoming_connections():
    while True:
        client, client_adress = SERVER.accept()
        client.send("Welcome to ANAN. Write 'SHUFFLE' to connect someone".encode())
        print("%s:%s has connected" % client_adress)
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    #Make sure that every client has a distinct id
    while 1:
        client_id=random.randint(0,100)
        if client_id not in list(clients.values()):
            clients[client]=client_id
            status[client_id]="AVAILABLE"
            break
        else:
            continue

    print(status)

    #Make sure that every client has a distinct peer



    while 1:
        msg = client.recv(1024).decode()
        print(str(clients[client])+":"+msg)
        if msg == "SHUFFLE":
            target_client = random.choice(list(clients.values()))
            if client_id!=target_client and status[target_client]=="AVAILABLE":
                match[client_id] = target_client
                status[client_id] = "FULL"
                status[target_client] = "FULL"
                client.send("You have been connected to someone!".encode())
                list(clients.keys())[list(clients.values()).index(target_client)].send(
                    "You have been connected to someone!".encode())




            else:
                continue



        else:
            frm = clients[client]
            try:
                to = match[frm]
            except KeyError:
                to = list(match.keys())[list(match.values()).index(frm)]

            to_client = list(clients.keys())[list(clients.values()).index(to)]
            to_client.send(msg.encode())


clients={}
status={}
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
