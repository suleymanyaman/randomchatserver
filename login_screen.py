import tkinter
import MySQLdb
from tkinter import messagebox



top = tkinter.Tk()
top.geometry("500x500")

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="members")
cursor = db.cursor()

label = tkinter.Label(top, text="Nickname:")
label.place(x=140, y=150)

user_id = tkinter.Entry(top)
user_id.place(x=210, y=150)

label_2 = tkinter.Label(top, text="Password:")
label_2.place(x=140, y=200)

password = tkinter.Entry(top, show="*")
password.place(x=210, y=200)

def auth_login(event=None):
    id = user_id.get()
    pswd = password.get()
    cursor.execute(
        "SELECT nickname, password FROM chatmembers WHERE nickname='{}' AND password='{}' ".format(id, pswd))
    if cursor.fetchone():
        top.destroy()


    else:
        messagebox.showerror("Wrong credentials", "Either nickname or password is wrong. Please try again.")

login_button = tkinter.Button(top, text="Log In", command=auth_login, height=2, width=20)
login_button.place(x=195, y=250)
top.mainloop()
