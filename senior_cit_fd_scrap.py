
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
#here we are importing various libraries that we would need to write up the code
def a():
    csv_file=open('csv/senior_cit_fd.csv','w')
    #creating a csv file
    csv_writer=csv.writer(csv_file)
    #opening in wriitng format
    csv_writer.writerow(['fixed_dep_with_bank_name','less_than_one_year', 'one_to_five_year', 'more_than_five'])
    #writing the row headings
    source = requests.get('https://www.bankbazaar.com/fixed-deposit/senior-citizen-fixed-deposit.html').text
    #website through which we are scrapping the data
    soup = BeautifulSoup(source,'lxml')
    senior_table = soup.find_all('table', class_='table table-bordered table-striped')[1].tbody.find_all('tr')
    #print(senior_table)
    for i in range(1,len(senior_table)):
        fixed_dep_with_bank_name = senior_table[i].find_all('td')[0].text
        print(fixed_dep_with_bank_name)
        #finding things that we want from the website and storing it in variable
        less_than_one_year = senior_table[i].find_all('td')[1].text
        print(less_than_one_year)
        one_to_five_year = senior_table[i].find_all('td')[2].text
        print(one_to_five_year)
        more_than_five = senior_table[i].find_all('td')[3].text
        print(more_than_five)

        csv_writer.writerow([fixed_dep_with_bank_name,less_than_one_year, one_to_five_year, more_than_five])
        #finding things that we want from the website and storing it in variable

    csv_file.close()
    files = pd.read_csv('csv/senior_cit_fd.csv')

    def func(file):
        row = []
        avg = []
        for i in range(len(file)):
            file['less_than_one_year'].iloc[i] = file['less_than_one_year'].iloc[i].replace('to', '')
            file['less_than_one_year'].iloc[i] = file['less_than_one_year'].iloc[i].replace('p.a.', '')
            file['less_than_one_year'].iloc[i] = file['less_than_one_year'].iloc[i].replace('%', '')

            file['one_to_five_year'].iloc[i] = file['one_to_five_year'].iloc[i].replace('to', '')
            file['one_to_five_year'].iloc[i] = file['one_to_five_year'].iloc[i].replace('p.a.', '')
            file['one_to_five_year'].iloc[i] = file['one_to_five_year'].iloc[i].replace('%', '')

            file['more_than_five'].iloc[i] = file['more_than_five'].iloc[i].replace('to', '')
            file['more_than_five'].iloc[i] = file['more_than_five'].iloc[i].replace('p.a.', '')
            file['more_than_five'].iloc[i] = file['more_than_five'].iloc[i].replace('%', '')
            
            
            

        return file


    new_file = func(files)

    df = pd.DataFrame(new_file)


    #df.to_csv('senior_cit_fd_1.csv')
    return df