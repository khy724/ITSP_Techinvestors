from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
#here we are importing various libraries that we would need to write up the code

def a():
    csv_file=open('india_bonds_3_5.csv','w')
    #creating a csv file

    csv_writer=csv.writer(csv_file)
    #opening in wriitng format

    csv_writer.writerow(['name','coupon','call_date','rating','type_of_bond','yeild','price'])
    #writing the row headings

    source = requests.get('https://www.indiabonds.com/search/?search=&maturity_date__gte=30%2F6%2F2024&maturity_date__lte=30%2F6%2F2026&limit=9&switch_one=radio-grid').text
    #website through which we are scrapping the data

    soup = BeautifulSoup(source,'lxml')
    #print(soup.prettify())
    table=soup.find_all('div',class_='container company-block')
    for element in table:
        same_class_1 = element.find_all('p', class_='company-title p-no-margin')
        name = same_class_1[0]
        #finding things that we want from the website and storing it in variable

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
        #finding things that we want from the website and storing it in variable

    csv_file.close()
    df = pd.read_csv('india_bonds_3_5.csv')
    return df