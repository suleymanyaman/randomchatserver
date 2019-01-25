import tkinter
from tkinter import messagebox
import socket
import sys
from threading import Thread
import tkinter
from tkinter import messagebox


connection_status = "OFFLINE "


def gantihal(frame):
    frame.tkraise()

root = tkinter.Tk()
root.title("Chit-Chat")
root.geometry("300x300")


f1 = tkinter.Frame(root)
f2 = tkinter.Frame(root)


for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

 #Frame 1

nickname_label= tkinter.Label(f1, text="Nickname:")
nickname_label.pack()
nickname_label.place(x=50, y=100)

nickname_area = tkinter.Entry(f1)
nickname_area.pack()
nickname_area.place(x=115, y=100)

password_label = tkinter.Label(f1, text="Password:")
password_label.pack()
password_label.place(x=50, y=140)

password_area = tkinter.Entry(f1, show="*")
password_area.pack()
password_area.place(x=115, y=140)




s = socket.socket()

def auth_login(event=None):
    global password_area
    global connection_status
    username = nickname_area.get()
    pswd = password_area.get()
    if username == "admin" and pswd == "1234567":
        try:
            s.connect((HOST, PORT))
            connection_status = "ONLINE"
            s.send(username.encode("utf-8"))
            gantihal(f2)
            #messagebox._show("Rchat v1.0.", "Welcome to RChat !")
        except ConnectionRefusedError:
            messagebox.showerror("Server Error", "The server is not connected.")

    else:
        messagebox.showerror("Wrong credentials", "Either nickname or password is wrong. Please try again.")

    return username



login_button = tkinter. Button(f1, text="Log In" , command= lambda: auth_login(), height=2, width=10)
login_button.pack()
login_button.place(x=115, y=170)



# Frame 2


HOST=socket.gethostbyname(socket.gethostname())
PORT=5000

messages_frame = tkinter.Frame(f2)
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
        if connection_status == "ONLINE":
            data = s.recv(1024)
            if not data: sys.exit(0)
            msg_list.insert(tkinter.END, data.decode())



def send(event=None):
    message = auth_login() + entry_field.get("1.0", "end-1c")
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
            root.destroy()



entry_field = tkinter.Text(f2, height=5, width=150)
entry_field.bind("<Return>", send)
entry_field.pack(side=tkinter.LEFT)


send_button = tkinter.Button(f2, text="Send", command=send, height=2, width=20)
send_button.pack()



shuffle_button = tkinter.Button(f2, text="Shuffle", command=shuffle, height=2, width=20)
shuffle_button.pack(side=tkinter.BOTTOM)



root.protocol("WM_DELETE_WINDOW", on_closing)


t1=Thread(target=recv)
t1.start()





gantihal(f1)
root.mainloop()



