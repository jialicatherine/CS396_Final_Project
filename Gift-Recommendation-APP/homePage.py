import subprocess as sb_p
import tkinter as tk
from tkinter import *
import registerUser
import os
import Server
import user as u

Server_path = os.path.abspath(os.getcwd())

def Home(root, frame1):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    root.title("Home")

    Label(frame1, text="Home", font=('Helvetica', 25, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    # Run server
    runServer = Button(frame1, text="Run Server", width=15, command = lambda: os.system("osascript -e \'tell application \"Terminal\" to do script \"cd "+Server_path+" && python3 Server.py\"\'"))

    frame2 = root.winfo_children()[0]
    #User Register
    register = Button(frame1, text="User Register", width=15, command = lambda: registerUser.Register(root, frame1, frame2))
    #User Login
    user = Button(frame1, text="User Login", width=15, command = lambda: u.userLogin(root, frame1, frame2))


    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)
    Label(frame1, text="").grid(row = 6,column = 0)
    runServer.grid(row = 3, column = 1, columnspan = 2)
    register.grid(row = 5, column = 1, columnspan = 2)
    user.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    Home(root, frame1)


if __name__ == "__main__":
    new_home()

