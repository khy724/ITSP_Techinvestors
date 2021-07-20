import pandas as pd
import numpy as np


def a(day,amount):
    Data = pd.read_csv('small_cap.csv', parse_dates=True)
    top_5= []
    top= []
    
    amount= float(amount)
    data= np.array(Data)
    length=data.shape[0]

    temp= []
    for i in range (length):
        temp.append(data[i, day+ 1])

    today= []
    for i in range (length):
        today.append(data[i, 1])

    diff= []
    for i in range(length):
        diff.append(temp[i]- today[i])

    shares= []
    for i in range (length):
        shares.append(amount/today[i])

    temp1= []
    for i in range(length):
        temp1.append(diff[i]*shares[i])

    
    runner= -10000
    for i in range(length):
        if runner< temp1[i]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i)

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0] and i!= top[1]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0] and i!= top[1] and i!= top[2]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i)

    runner= -10000
    for i in range(length):
       
       if runner< temp1[i] and i!= top[0] and i!= top[1] and i!= top[2] and i!= top[3]:
            runner= temp1[i]
    for i in range(length):
       if temp1[i]== runner:
           top.append(i) 

    
    for i in range(5):
       
       top_5.append(data[top[i], 0])
    return top_5

def b(day,amount):
    Data = pd.read_csv('largecap_data.csv', parse_dates=True)
    top_5= []
    top= []
    
    amount= float(amount)
    data= np.array(Data)
    length=data.shape[0]

    temp= []
    for i in range (length):
        temp.append(data[i, day+ 1])

    today= []
    for i in range (length):
        today.append(data[i, 1])

    diff= []
    for i in range(length):
        diff.append(temp[i]- today[i])

    shares= []
    for i in range (length):
        shares.append(amount/today[i])

    temp1= []
    for i in range(length):
        temp1.append(diff[i]*shares[i])

    
    runner= -10000
    for i in range(length):
        if runner< temp1[i]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i)

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0] and i!= top[1]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0] and i!= top[1] and i!= top[2]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i)

    runner= -10000
    for i in range(length):
       
       if runner< temp1[i] and i!= top[0] and i!= top[1] and i!= top[2] and i!= top[3]:
            runner= temp1[i]
    for i in range(length):
       if temp1[i]== runner:
           top.append(i) 

    
    for i in range(5):
       
       top_5.append(data[top[i], 0])
    return top_5

def c(day,amount):
    Data = pd.read_csv('mid_cap.csv', parse_dates=True)
    top_5= []
    top= []

    amount= float(amount)
    data= np.array(Data)
    length=data.shape[0]

    temp= []
    for i in range (length):
        temp.append(data[i, day+ 1])

    today= []
    for i in range (length):
        today.append(data[i, 1])

    diff= []
    for i in range(length):
        diff.append(temp[i]- today[i])

    shares= []
    for i in range (length):
        shares.append(amount/today[i])

    temp1= []
    for i in range(length):
        temp1.append(diff[i]*shares[i])


    runner= -10000
    for i in range(length):
        if runner< temp1[i]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i)

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0] and i!= top[1]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 

    runner= -10000
    for i in range(length):
        if runner< temp1[i] and i!= top[0] and i!= top[1] and i!= top[2]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i)

    runner= -10000
    for i in range(length):
        
        if runner< temp1[i] and i!= top[0] and i!= top[1] and i!= top[2] and i!= top[3]:
            runner= temp1[i]
    for i in range(length):
        if temp1[i]== runner:
            top.append(i) 


    for i in range(5):
        
        top_5.append(data[top[i], 0])
    return top_5   
