import tkinter as tk
import socket
from tkinter import *
from HolidayPage import holidayPg
from homePage import Home

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'

def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,email,password):
    message = email + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        frame3 = root.winfo_children()[1]
        holidayPg(root, frame1, frame3, client_socket)

    elif(message=="Online"):
        message = "User has Already Logged In"
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidEmail"):
        message = "Invalid Email"
        failed_return(root,frame1,client_socket,message)

    elif(message=="WrongPassw"):
        message = "Wrong Password"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)

def userLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("User Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="User Login", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Email:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:   ", anchor="e", justify=LEFT).grid(row = 3,column = 0)

    Email = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = Email)
    e1.grid(row = 2,column = 2)
    e3 = Entry(frame1, textvariable = password, show = '*')
    e3.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=10, command = lambda: log_server(root, frame1, client_socket, Email.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         userLogin(root,frame1)
