import tkinter as tk
import dframe as df
from tkinter import ttk
from tkinter import *
from dframe import *
import socket
import homePage

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'

def failed_return(root,frame1,frame2,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame2, text="Home", command = lambda: homePage.Home(root, frame1)).grid(row=0,column=0)
    frame2.pack(side=TOP)

    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def registeredPg(root,frame1,frame2,client_socket,name):
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame2, text="Home", command = lambda: homePage.Home(root, frame1)).grid(row=0,column=0)
    frame2.pack(side=TOP)

    txt = "Successfully Registered \n\n Welcome " + str(name) + "\n\n Now you can go login"
    Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)
    client_socket.close()

def reg_server(root,frame1,frame2,client_socket,email,name,sex,state,city,passw):
    if(passw=='' or passw==' '):
        msg = Message(frame1, text="Error: Missing Fileds", width=500)
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1
    message = "register " + email + " " + name + " " + sex + " " + state + " " + city + " " + passw
    client_socket.send(message.encode())

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        registeredPg(root,frame1,frame2,client_socket,name)

    elif(message=="ExistedUser"):
        message = "This email has already been registered"
        failed_return(root,frame1,frame2,client_socket,message)
    
    elif(message=="InvalidEmail"):
        message = "Invalid Email Format"
        failed_return(root,frame1,frame2,client_socket,message)

    elif(message=="EmptyInput"):
        message = "Input Cannot be Empty"
        failed_return(root,frame1,frame2,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,frame2,client_socket,message)


def Register(root,frame1,frame2):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,frame2,client_socket,message)
    
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame2, text="Home", command = lambda: homePage.Home(root, frame1)).grid(row=0,column=0)
    frame2.pack(side=TOP)

    root.title("Register User")

    Label(frame1, text="Register User", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Email:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Name:         ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Label(frame1, text="Sex:              ", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    Label(frame1, text="State:           ", anchor="e", justify=LEFT).grid(row = 5,column = 0)
    Label(frame1, text="City:             ", anchor="e", justify=LEFT).grid(row = 6,column = 0)
    Label(frame1, text="Password:   ", anchor="e", justify=LEFT).grid(row = 7,column = 0)

    email = tk.StringVar()
    name = tk.StringVar()
    sex = tk.StringVar()
    state = tk.StringVar()
    city = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = email).grid(row = 2, column = 2)
    e2 = Entry(frame1, textvariable = name).grid(row = 3, column = 2)
    e5 = Entry(frame1, textvariable = state).grid(row = 5, column = 2)
    e6 = Entry(frame1, textvariable = city).grid(row = 6, column = 2)
    e7 = Entry(frame1, textvariable = password).grid(row = 7, column = 2)

    e4 = ttk.Combobox(frame1, textvariable = sex, width=17)
    e4['values'] = ("Male","Female","Transgender")
    e4.grid(row = 4, column = 2)
    e4.current()

    reg = Button(frame1, text="Register", command = lambda: reg_server(root, frame1, frame2, client_socket, email.get(), name.get(), sex.get(), state.get(), city.get(), password.get()), width=10)
    Label(frame1, text="").grid(row = 8,column = 0)
    reg.grid(row = 9, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         Register(root,frame1)
