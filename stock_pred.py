#importing all libraries
import pandas as pd                                        
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

import yfinance as yf

from plotly import graph_objs as go
from datetime import date

from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense, LSTM, Dropout
#deciding the start day and setting the end day for prediction training data as the present day
start="2018-05-01"
today=date.today().strftime("%Y-%m-%d")
stocks= ('BRITANNIA.NS','3MINDIA.NS', 'ADANIPORTS.NS','ABCAPITAL.NS', 'ALKEM.NS', 'AMBUJACEM.NS', 'ASHOKLEY.NS', 'ASIANPAINT.NS', 'AUROPHARMA.NS', 'DMART.NS', 'AXISBANK.NS', 'BHEL.NS', 'BPCL.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJAJHLDNG.NS', 'BANDHANBNK.NS', 'BANKBARODA.NS', 'BERGEPAINT.NS', 'BEL.NS', 'BHARATFORG.NS', 'BHARTIARTL.NS', 'CADILAHC.NS', 'CANBK.NS', 'CASTROLIND.NS', 'CHOLAFIN.NS', 'CIPLA.NS', 'COALINDIA.NS', 'COLPAL.NS', 'DABUR.NS', 'DALMIASUG.NS', 'DLF.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'EMAMILTD.NS', 'FRETAIL.NS', 'GAIL.NS', 'GICRE.NS', 'GILLETTE.NS' ,'GODREJCP.NS' ,'HDFCBANK.NS', 'HAVELLS.NS', 'HCLTECH.NS', 'HEROMOTOCO.NS', 'HINDUNILVR.NS', 'HAL.NS', 'HINDALCO.NS', 'ICICIBANK.NS', 'IBULHSGFIN.NS', 'IGL.NS', 'INFY.NS', 'ITC.NS', 'JINDALSTEL.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'KOTAKBANK.NS', 'LUPIN.NS', 'MARICO.NS', 'MARUTI.NS')
#attaining stock data from yfinance
def inp_data(ticker):
    data= yf.download(ticker, start, today)
    data. reset_index(inplace=True)
    return data
# whatever ticker is entered as stockname, that stocks data is stored in data1
stock_name= '3MINDIA.NS'
data1= inp_data(stock_name)
#only retaining the closing price from data1
data1= data1.reset_index()['Close']
#checking for nan
data1.isna().sum()
# using minmax scaler to scale the data 
scaler= MinMaxScaler(feature_range=(0,1))
data1= scaler.fit_transform(np.array(data1).reshape(-1,1))
#todays_price= data1[data1.shape[0]-1:, 0]
#todays_price= todays_price.reshape(-1,1)
#todays_price=scaler.inverse_transform(todays_price)
#todays_price=list(todays_price)
#todays_price= todays_price[0].tolist()
#todays_price= todays_price[0]
#todays_price
# forming the trainingsets, using previous 100 days data to predict the present day data
#havent fromed a test set in this code but weve tried it on a test set too and that works fine
training_size= data1.shape[0]
print(training_size)
time_step= 100
x_train= []
y_train= []

for i in range(time_step, training_size):
    x_train.append(data1[i-100:i, 0])
    y_train.append(data1[i,0])
x_train, y_train= np.array(x_train), np.array(y_train)
    
x_train.shape, y_train.shape
#reshaping to a 3D array
x_train= x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
# building the model
regressor= Sequential()

regressor.add(LSTM(units= 256, activation= 'relu',return_sequences= True, input_shape= (x_train.shape[1],x_train.shape[2])))
regressor.add(Dropout(0.2))

#regressor.add(LSTM(units= 60, activation= 'relu',return_sequences= True))
#regressor.add(Dropout(0.3))

#regressor.add(LSTM(units= 80, activation= 'relu',return_sequences= True))
#regressor.add(Dropout(0.4))

regressor.add(LSTM(units= 256, activation= 'relu'))
regressor.add(Dropout(0.4))

regressor.add(Dense(units= 1))
 #used adam as an optimizer
regressor.compile( optimizer= 'adam', loss= 'mean_squared_error', metrics= ['accuracy'])
#training the data
regressor.fit(x_train, y_train, epochs= 50, batch_size= 32, verbose= 1)
#prediction of the stock prices using the model and test set 
train_pred= regressor.predict(x_train)
train_pred= scaler.inverse_transform(train_pred)
#train_pred, train_pred.shape
train_pred.shape
# calculating the error
import math 
from sklearn.metrics import mean_squared_error
#y_train.shape
math.sqrt(mean_squared_error(y_train, train_pred))
#plotting actual prices vs predicted prices
plt.figure(figsize=(17,7))
plt.plot(train_pred, color= 'red')

y_train=y_train.reshape(-1, 1)
#print(y_train)
y_train= scaler.inverse_transform(data1)
#print(y_train)
plt.plot(y_train[100:], color= 'yellow')
plt.show()
# x_input contains the past 100 days stock prices from the present day
length= len(data1)
x_input= data1[length- 100:]
x_input= np.array(x_input)
x_input= x_input.reshape(1, -1)
x1=x_input
x_input.shape
x1.shape
temp_input= list(x_input)
#temp_input= temp_input[0].tolist()
temp_input= temp_input[0].tolist()
# predicting the stock price for the next 30 days from the present day
n_steps= 100
i= 0
output= []
days_pred= 60

while i<days_pred:
    
    if(len(temp_input)>100):
        x_input= np.array(temp_input[1:])
       # print(" {} day input {} ".format(i, x_input))
        x_input= x_input.reshape(1, -1)
        x_input= x_input.reshape((1, n_steps, 1))
        y= regressor.predict(x_input)
        #print(" {} day output {} ".format(i, y))
        temp_input.extend(y[0].tolist())
        temp_input= temp_input[1: ]
        output.extend(y.tolist())
        i=i+1
    else:
        x_input= x_input.reshape((1, n_steps, 1))
        y= regressor.predict(x_input)
        #print(y[0])
        temp_input.extend(y[0].tolist())
       # print(len(temp_input))
        output.extend(y.tolist())
        i=i+1

output= np.array(output)
output= output.reshape(-1, 1)
x1= list(x1)
x1=x1[0].tolist()
#print(len(x1))

#initial x has numbers from 1 to 100 and final x from 101 to 160
initialx= np.arange(1,len(x1)+1)
finalx = np.arange(len(x1)+1, len(x1)+1+days_pred)

x1= np.array(x1)
x1= x1.reshape(-1, 1)
#plotting the actual and predicted values
plt.plot( initialx, train_pred[length- 200:])
plt.plot( finalx, scaler.inverse_transform(output))
plt.plot(initialx, scaler.inverse_transform(data1[length- 100:]))
plt.show()

#converting the predicted data to a list
output= scaler.inverse_transform(output)
output= output.reshape(1, -1)
output= list(output)
#output
output= output[0].tolist()
#output
output.insert(0,todays_price	)
output.insert(0,stock_name)
#importing a csv file in whick we store the 60 days stock price for all stocks
from google.colab import files
files.upload()

Data = pd.read_csv('Data (1).csv', parse_dates=True)
import csv
file= open('Data (1).csv', 'a+', newline= '')
with file:
  write= csv.writer(file)
  write.writerows(data)

#data=pd.read_csv('predicted_values.csv',date_parser=True)
#data.head()
Data= pd.read_csv('Data (1).csv', parse_dates=True)

Data.to_csv('Data.csv',index= False)
! ls
!cat Data.csv
