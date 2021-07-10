from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def a(cs):
    csv_file=open(str(cs),'w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Banks','interest_rate'])
    source = requests.get('https://www.paisabazaar.com/fixed-deposit/all-banks/').text
    soup = BeautifulSoup(source,'lxml')
    #print(soup.prettify())
    data_table=soup.find_all('tr')
    #print()


    for i in range(2,len(data_table)):
        bank_name = data_table[i].find_all('span',style="font-weight: 400;")[0].text
        print(bank_name)
        interest_rate = data_table[i].find_all('span',style="font-weight: 400;")[1].text
        print(interest_rate)


        csv_writer.writerow([bank_name,interest_rate])

    csv_file.close()
    df = pd.read_csv('fd_data.csv')
    return df
    '''for every_elem in data_table:

        bank_name = every_elem[0]
        print(bank_name.text)
        interest_rate = every_elem[1]
        print(interest_rate.text)'''


