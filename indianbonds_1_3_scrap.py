from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
def a():
    csv_file=open('india_bonds_1_3.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['name','coupon','call_date','rating','type_of_bond','yeild','price'])
    source = requests.get('https://www.indiabonds.com/search/?search=&maturity_date__gte=30%2F6%2F2022&maturity_date__lte=30%2F6%2F2024&limit=9&switch_one=radio-grid').text
    soup = BeautifulSoup(source,'lxml')
    #print(soup.prettify())
    table=soup.find_all('div',class_='container company-block')
    for element in table:
        same_class_1 = element.find_all('p', class_='company-title p-no-margin')
        name = same_class_1[0]
        print(name.text)
        same_class = element.find_all('p',class_='info-value')
        coupon = same_class[0]
        print(coupon.text)
        call_date = same_class[1]
        print(call_date.text)
        rating = same_class[2]
        print(rating.text)
        type_of_bond = same_class[3]
        print(type_of_bond.text)
        yeild = element.find('p',class_='info-value tan-colored')
        print(yeild.text)
        price = same_class[5]
        print(price.text)
        csv_writer.writerow([name.text,coupon.text,call_date.text,rating.text,type_of_bond.text,yeild.text,price.text])

    csv_file.close()
    df = pd.read_csv('india_bonds_1_3.csv')
    return df









