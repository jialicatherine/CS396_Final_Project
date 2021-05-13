import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image
import HolidayPage 


def userLogout(root,frame1,frame3,client_socket):
    client_socket.send("Logout".encode()) 

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="LoggedOut"):
        for widget in frame1.winfo_children():
            widget.destroy()
        txt = "You have successfully logged out!"
        Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)
        root.quit()
        client_socket.close()
    else: 
        message = "Server Error"
        for widget in frame1.winfo_children():
            widget.destroy()
            message = message + "... \nTrying again..."
        Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
        userLogout(root,frame1,frame3,client_socket)

def keepChoosing(root,frame1,frame3,client_socket):
    client_socket.send("keepChoosing".encode())
    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if (message == 'ChooseAgain'):
        HolidayPage.holidayPg(root,frame1,client_socket)
    else: 
        message = "Server Error"
        for widget in frame1.winfo_children():
            widget.destroy()
            message = message + "... \nTrying again..."
        Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
        keepChoosing(root,frame1,frame3,client_socket)    

def recPg(root,frame1,frame3,rec,client_socket):

    root.title("Recommendation")
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame3, text="Choose Holiday", command = lambda: keepChoosing(root, frame1, frame3,client_socket)).grid(row = 1, column = 0)
    frame3.pack(side=TOP)

    txt = "Gift Recommendation: \n\n" + rec 
    Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)

    logout = Button(frame1, text="Logout", width=10, command = lambda: userLogout(root, frame1,frame3,client_socket))
    Label(frame1, text="").grid(row = 4,column = 0)
    logout.grid(row = 8, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         recPg(root,frame1,frame3,rec,client_socket)
