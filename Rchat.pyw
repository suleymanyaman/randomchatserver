import socket
import sys
from threading import Thread
import tkinter
from tkinter import messagebox

HOST="68.183.210.79"
PORT=5000


top = tkinter.Tk()
top.state("zoomed")
top.title("RChat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Type your messages here")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=37, width=200, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()





def recv():
    while True:
        data = s.recv(1024)
        if not data: sys.exit(0)
        msg_list.insert(tkinter.END, data.decode())




def send(event=None):
    message = entry_field.get("1.0", "end-1c")
    s.send(message.encode('utf-8'))
    entry_field.delete('1.0', tkinter.END)
    return "break"


def shuffle(event=None):
    s.send("?pRG=gmxHD74cEm".encode("utf-8"))



def on_closing(event=None):
    if messagebox.askokcancel("Quit", "Do you want to quit RChat?"):
        try:
            s.send("4t7w!z%C".encode("utf-8"))
        finally:
            top.destroy()





try:
    s = socket.socket()
    s.connect((HOST,PORT))

except ConnectionRefusedError:
    msg_list.insert(tkinter.END, "The server is not connected.")





entry_field = tkinter.Text(top, height=5, width=150)
entry_field.bind("<Return>", send)
entry_field.place(x=72, y=600)



send_button = tkinter.Button(top, text="Send", command=send, height=2, width=20)
send_button.pack()
send_button.place(x=1150, y=600)



shuffle_button = tkinter.Button(top, text="Shuffle", command=shuffle, height=2, width=20)
shuffle_button.pack()
shuffle_button.place(x=1150, y=650)

top.protocol("WM_DELETE_WINDOW", on_closing)


t1=Thread(target=recv)
t1.start()
tkinter.mainloop()
