import pandas as pd
import re
import os

path = os.getcwd()+'/database'

def verify(email,passw):
    df=pd.read_csv(path+'/userList.csv')
    df=df[['Email','Passw']]
    for index, row in df.iterrows():
        if str(df['Email'].iloc[index])==str(email) and str(df['Passw'].iloc[index])==str(passw):
            return True
    return False

def Existed(email):
    df=pd.read_csv(path+'/userList.csv')
    df=df[['Email']]
    for index, row in df.iterrows():
        if df['Email'].iloc[index]==email:
            return True
    return False

def validEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    if(re.search(regex, email)):
        return True

def isEligible(email):
    df=pd.read_csv(path+'/userList.csv')
    df=df[['Email','Name','Gender','State','City','Passw','Online']]
    for index, row in df.iterrows():
        if df['Email'].iloc[index]==email and df['Online'].iloc[index]==0:
            return True
    return False

def login(email):
    df=pd.read_csv(path+'/userList.csv')
    df=df[['Email','Name','Gender','State','City','Passw','Online', 'Holiday']]
    for index, row in df.iterrows():
        if df['Email'].iloc[index]==email:
            df['Online'].iloc[index]=1
    df.to_csv(path+'/userList.csv')

def logout(email):
    df=pd.read_csv(path+'/userList.csv')
    df=df[['Email','Name','Gender','State','City','Passw','Online', 'Holiday']]
    for index, row in df.iterrows():
        if df['Email'].iloc[index]==email:
            df['Online'].iloc[index]=0
    df.to_csv(path+'/userList.csv')

def add_holiday(holiday,email):
    if validEmail(email) and str(holiday) != '':
        df=pd.read_csv(path+'/userList.csv')
        df=df[['Email','Name','Gender','State','City','Passw','Online', 'Holiday']]
        for index, row in df.iterrows():
            if str(df['Email'].iloc[index])==str(email):
                if str(df['Holiday'].iloc[index]) == 'nan':
                    df['Holiday'].iloc[index] = str(holiday)
                else:
                    holidaylst = str(df['Holiday'].iloc[index]).split(',')
                    if holiday not in holidaylst:
                        holidaylst.append(holiday)
                    holidays = ','.join(holidaylst)
                    df['Holiday'].iloc[index]= holidays
        df.to_csv(path+'/userList.csv')
        return True
    return False

def taking_data_user(email, name,gender,state,city,passw):
    df=pd.read_csv(path+'/userList.csv')
    df=df[['Email','Name','Gender','State','City','Passw','Online','Holiday']]
    row,col=df.shape
    df1 = pd.DataFrame({"Email":[email],
                "Name":[str(name)],
                "Gender":[str(gender).lower()],
                "State":[str(state).lower()],
                "City":[str(city).lower()],
                "Passw":[str(passw)],
                "Online":[0],
                "Holiday":['']},)
    df=df.append(df1,ignore_index=True)
    df.to_csv(path+'/userList.csv')
    return name
