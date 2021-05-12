import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

GiftRec = {"christmas":"Scented Candle", "halloween":"Totoro Custome", "birthday":"Switch!", "valentine":"Microwaveable Toys", "graduation":"Champagne" }

def userLogout(root,frame1,client_socket):
    client_socket.send("Logout".encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="LoggedOut"):
        client_socket.close()
        print("You have Logged Out")
        root.quit()
    else:
        message = "Server Error"
        for widget in frame1.winfo_children():
            widget.destroy()
            message = message + "... \nTry again..."
        Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
        holidayPg(root, frame1, client_socket)

def chooseHoliday(root,frame1,holiday,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(holiday.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Holiday Successfully Chosen", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
        for widget in frame1.winfo_children():
            widget.destroy()
        gift = GiftRec[holiday]
        txt = "Gift Recommendation: \n\n" + gift + "\n\n Now you can go login"
        Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)
    else:
        text = "Holiday Failed to be Chosen"
        msg = Message(frame1, text=text, width=500)
        msg.grid(row = 6, column = 0, columnspan = 5)

def holidayPg(root,frame1,frame3,client_socket):

    root.title("Holiday")
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame1, text="Choose Holiday", command = lambda: holidayPg(root, frame1, frame3,client_socket)).grid(row = 1, column = 0)
    frame3.pack(side=TOP)

    Label(frame1, text="Choose a Holiday", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    holiday = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "Christmas", variable = holiday, value = "christmas", indicator = 0, height = 4, width=15, command = lambda: chooseHoliday(root,frame1,"christmas",client_socket)).grid(row = 2,column = 1)
    christmasLogo = ImageTk.PhotoImage((Image.open("img/christmas.png")).resize((45,45),Image.ANTIALIAS))
    christmasImg = Label(frame1, image=christmasLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Halloween", variable = holiday, value = "halloween", indicator = 0, height = 4, width=15, command = lambda: chooseHoliday(root,frame1,"halloween",client_socket)).grid(row = 3,column = 1)
    halloweenLogo = ImageTk.PhotoImage((Image.open("img/Halloween.png")).resize((35,48),Image.ANTIALIAS))
    halloweenImg = Label(frame1, image=halloweenLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Birthday", variable = holiday, value = "birthday", indicator = 0, height = 4, width=15, command = lambda: chooseHoliday(root,frame1,"birthday",client_socket) ).grid(row = 4,column = 1)
    birthdayLogo = ImageTk.PhotoImage((Image.open("img/birthday.png")).resize((45,45),Image.ANTIALIAS))
    birthdayImg = Label(frame1, image=birthdayLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Valentine's Day", variable = holiday, value = "valentine", indicator = 0, height = 4, width=15, command = lambda: chooseHoliday(root,frame1,"valentine",client_socket)).grid(row = 5,column = 1)
    valentineLogo = ImageTk.PhotoImage((Image.open("img/valentine.png")).resize((50,45),Image.ANTIALIAS))
    valentineImg = Label(frame1, image=valentineLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "Graduation Day", variable = holiday, value = "graduation", indicator = 0, height = 4, width=15, command = lambda: chooseHoliday(root,frame1,"graduation",client_socket)).grid(row = 6,column = 1)
    graduationLogo = ImageTk.PhotoImage((Image.open("img/graduation.png")).resize((45,35),Image.ANTIALIAS))
    graduationImg = Label(frame1, image=graduationLogo).grid(row = 6,column = 0)

    logout = Button(frame1, text="Logout", width=10, command = lambda: userLogout(root, frame1, client_socket))
    Label(frame1, text="").grid(row = 4,column = 0)
    logout.grid(row = 8, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         holidayPg(root,frame1,client_socket)
