import yfinance as yf
import pandas as pd
from datetime import date
import numpy as np
def inp_data(ticker1):
    start="2020-07-14"
    today=date.today().strftime("%Y-%m-%d")
    data= yf.download(ticker1, start, today)
    data.reset_index(inplace=True)
    return data
def a(stock_list):
    
    data1= inp_data(str(stock_list[0]))
    data1= data1.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume','Date'], axis= 1)
    data2= inp_data(str(stock_list[1]))
    data2= data2.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume','Date'], axis= 1)
    data3= inp_data(str(stock_list[2]))
    data3= data3.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume','Date'], axis= 1)
    data4= inp_data(str(stock_list[3]))
    data4= data4.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume','Date'], axis= 1)
    data5= inp_data(str(stock_list[4]))
    data5= data5.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume','Date'], axis= 1)
    data_1= np.array(data1)
    data_2= np.array(data2)
    data_3= np.array(data3)
    data_4= np.array(data4)
    data_5= np.array(data5)
    #index = []
    data_final=[]
    for i in range(len(data_1)):
        l= []
        l.append(i)
        l.append(float(data_1[i]))
        l.append(float(data_2[i]))
        l.append(float(data_3[i]))
        l.append(float(data_4[i]))
        l.append(float(data_5[i]))
        data_final.append(l)
      
    return data_final

