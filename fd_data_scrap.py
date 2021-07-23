from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
#here we are importing various libraries that we would need to write up the code

def a():
    csv_file = open('csv/fd_data.csv', 'w')
    #creating a csv file
    csv_writer = csv.writer(csv_file)
    #opening in wriitng format
    csv_writer.writerow(['Banks', 'interest_rate'])
    #writing the row headings
    source = requests.get('https://www.paisabazaar.com/fixed-deposit/all-banks/').text
    #website through which we are scrapping the data
    soup = BeautifulSoup(source, 'lxml')
    data_table = soup.find_all('tr')

    for i in range(2, len(data_table)):
        bank_name = data_table[i].find_all('span', style="font-weight: 400;")[0].text
        print(bank_name)
        #finding things that we want from the website and storing it in variable
        interest_rate = data_table[i].find_all('span', style="font-weight: 400;")[1].text
        print(interest_rate)

        csv_writer.writerow([bank_name, interest_rate])
        #finding things that we want from the website and storing it in variable

    csv_file.close()
    df = pd.read_csv('csv/fd_data.csv')
    return df

file = pd.read_csv('csv/fd_data.csv')

def func(file):
    for i in range(len(file['interest_rate'])):
        file['interest_rate'].iloc[i] = file['interest_rate'].iloc[i].replace('Up', '')
        file['interest_rate'].iloc[i] = file['interest_rate'].iloc[i].replace('to', '')
        file['interest_rate'].iloc[i] = file['interest_rate'].iloc[i].replace('%', '')
    return file
    #since we were getting unwanted strings from scrapping so we replaced those

def b(abc):
    

    '''abc.drop('Unnamed: 0', inplace=True, axis=1)'''


    abc.to_csv('csv/fd_data_new.csv')
    sorted_df = abc.sort_values(by=["interest_rate"], ascending=False)
    #sorting the data based on interest rate
    sorted_df.to_csv('csv/fd_data_final.csv', index=False)
    return sorted_df
