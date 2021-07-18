from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
def a():
    csv_file=open('dividend_stock.csv','w')

    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['company_name ','p/e_ratio', '1_yr_return_pr', 'payout_ratio_pr', '3_yr_avg_div_payout','prize_value','1_yr_profit_growth_pr'])
    source = requests.get('https://wikifinancepedia.com/investing/investment/top-10-best-dividend-stocks-long-term-retirement-income-india').text
    soup = BeautifulSoup(source,'lxml')
    #print(soup.prettify())
    table = soup.find_all('figure', class_="wp-block-table is-style-stripes")
    #print(table[0])
    table_final = table[0]

    table_row = table_final.find_all('tr')
    for i in range(1,len(table_row)):
        company_name = table_row[i].find_all('td')[1].text
        #print(company_name)
        p_e_ratio = table_row[i].find_all('td')[2].text

        #print(p_e_ratio)
        one_yr_return_pr = table_row[i].find_all('td')[3].text
        #print(one_yr_return_pr)
        payout_ratio_pr = table_row[i].find_all('td')[4].text

        #print(payout_ratio_pr)
        ##
        three_yr_avg_div_payout = table_row[i].find_all('td')[5].text
        prize_value = table_row[i].find_all('td')[6].text

        ##
        one_yr_profit_growth_pr = table_row[i].find_all('td')[7].text

        csv_writer.writerow([company_name,p_e_ratio,one_yr_return_pr,payout_ratio_pr,three_yr_avg_div_payout,prize_value,one_yr_profit_growth_pr])


    csv_file.close()
    df = pd.read_csv('dividend_stock.csv')
    return df