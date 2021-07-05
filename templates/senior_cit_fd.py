from bs4 import BeautifulSoup
import requests
import csv
csv_file=open('senior_cit_fd.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['fixed_dep_with_bank_name','less_than_one_year', 'one_to_five_year', 'more_than_five'])
source = requests.get('https://www.bankbazaar.com/fixed-deposit/senior-citizen-fixed-deposit.html').text
soup = BeautifulSoup(source,'lxml')
senior_table = soup.find_all('table', class_='table table-bordered table-striped')[1].tbody.find_all('tr')
#print(senior_table)
for i in range(1,len(senior_table)):
    fixed_dep_with_bank_name = senior_table[i].find_all('td')[0].text
    print(fixed_dep_with_bank_name)
    less_than_one_year = senior_table[i].find_all('td')[1].text
    print(less_than_one_year)
    one_to_five_year = senior_table[i].find_all('td')[2].text
    print(one_to_five_year)
    more_than_five = senior_table[i].find_all('td')[3].text
    print(more_than_five)

    csv_writer.writerow([fixed_dep_with_bank_name,less_than_one_year, one_to_five_year, more_than_five])

csv_file.close()