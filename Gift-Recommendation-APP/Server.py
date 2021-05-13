import socket
import threading
import dframe as df
from threading import Thread
from dframe import *
import traceback
import time

#Database
GiftRec = {"christmas":"Scented Candle", "halloween":"Totoro Custome", "birthday":"Switch!", "valentine":"Microwaveable Toys", "graduation":"Champagne" }


lock = threading.Lock()

# Get Holiday Choice
def chooseHoliday(connection, receive):
    data2 = connection.recv(1024)
    receive2 = data2.decode()
    print("Holiday Chosen by User: "+str(receive[0])+"  Processing...")
    #update Database
    if(df.add_holiday(receive2,receive[0])):
        print("User: "+str(receive[0])+" chose "+str(receive2))
        send = "Successful"+" "+GiftRec[receive2]
        connection.send(send.encode())
    else:
        print("Holiday Failed to be Chosen by User: "+str(receive[0]))
        connection.send("Failed".encode())

def client_thread(connection, address):
    data = connection.recv(1024)     
    # registering new user ---Option 1.1
    receive = (data.decode()).split(' ')

    if (receive[0]=='register'):
        if (df.validEmail(receive[1])):
            if not df.Existed(receive[1]):
                for i in receive[2:]:
                    if (i == ''):
                        print('Empty Input')
                        connection.send("EmptyInput".encode())
                print('User '+str(receive[2])+' Registered')
                df.taking_data_user(receive[1], receive[2], receive[3], receive[4], receive[5], receive[6])
                connection.send("Authenticate".encode())
            else:
                print('Email Already Registered:'+str(receive[1]))
                connection.send("ExistedUser".encode())
        else:
            print('Invalid Email Format')
            connection.send("InvalidEmail".encode())
            
    else:
        #verify user details ---Option 1.2
        print("Entered Login")
        if (validEmail(receive[0])):
            print("Entered Valid Email")
            if(df.verify(receive[0],receive[1])):   
                print("Entered Correct Password")                            
                if(df.isEligible(receive[0])):
                    print('User Logged in... Email:'+str(receive[0]))
                    df.login(receive[0])
                    connection.send("Authenticate".encode())

                    # Choose Holiday ---Option 2.1
                    chooseHoliday(connection, receive)

                    # Keep choosing holidays or logout
                    Loggedout = False
                    while not Loggedout:
                        data3 = connection.recv(1024)
                        receive3 = data3.decode()
                        
                        if (receive3 == 'Logout'): # ---Option 3.1
                            connection.send("LoggedOut".encode())
                            df.logout(receive[0]) 
                            Loggedout = True   
                        else:                      # ---Option 3.2
                            connection.send("ChooseAgain".encode())
                            chooseHoliday(connection, receive)

                else:
                    print('User Already Logged In: '+str(receive[0]))
                    connection.send("Online".encode())
            else:
                print('Wrong Password')
                connection.send("WrongPassw".encode())
        else:
            print('Invalid Email')
            connection.send("InvalidEmail".encode())
               
    connection.close()
    print("Connection "+address+" Closed!")

def Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)
        ip, port = str(address[0]), str(address[1])
        addressstr = ip + ":" + port
        client.send("Connection Established".encode())   
        t = Thread(target = client_thread,args = (client,addressstr))
        try:
            t.start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    Server()
