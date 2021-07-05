from bs4 import BeautifulSoup
import requests
import csv
csv_file=open('mutual_funds.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_w_pr','1_m_pr', '3_m_pr','6_m_pr','1_y_pr','3_y_pr','5_y_pr'])

source = requests.get('https://www.mutualfundindia.com/').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

equity_mf_table = soup.find('div', id='topFundEquity' , class_='tab-pane fade active in').find('tbody').find_all('tr')
#print(equity_mf_table)
#find('tbody').find_all('tr')
#print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
print(equity_mf_table[0].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0,10):
    fund_name = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = equity_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    #print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = equity_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = equity_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = equity_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow([fund_name, category, aum_rs_cr, one_w_pr.text,one_m_pr, three_m_pr,six_m_pr,one_y_pr,three_y_pr,five_y_pr])

balanced_mf_table = soup.find('div', id='topFundBalanced').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
print(balanced_mf_table[1].find('td',style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = balanced_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = balanced_mf_table[i].find('td',style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = balanced_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = balanced_mf_table[i].find('td',style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])

debt_mf_table = soup.find('div', id='topFundDebt').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = debt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = debt_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = debt_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = debt_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])




liquid_mf_table = soup.find('div', id='topFundLiquid').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = liquid_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = liquid_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = liquid_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = liquid_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])


gilt_mf_table = soup.find('div', id='topFundGilt').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = gilt_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = gilt_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = gilt_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = gilt_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])


dynamic_mf_table = soup.find('div', id='topFundDynamic').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = dynamic_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = dynamic_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = dynamic_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = dynamic_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])

etf_mf_table = soup.find('div', id='topFundETF').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = etf_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = etf_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = etf_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = etf_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])


speciality_mf_table = soup.find('div', id='topFundSpeciality').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = speciality_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = speciality_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = speciality_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = speciality_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])

fof_mf_table = soup.find('div', id='topFundFOF').find('tbody').find_all('tr')
# print(funds_table[1].find_all('td',style="line-height: 12px; font-size: 11px!important")[0].text)
#print(debt_mf_table[1].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text)

for i in range(0, 10):
    fund_name = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[0].text
    print(fund_name)
    category = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[1].text
    print(category)
    one_m_pr = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[2].text
    print(one_m_pr)
    three_m_pr = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[3].text
    print(three_m_pr)
    six_m_pr = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[4].text
    print(six_m_pr)
    three_y_pr = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[5].text
    print(three_y_pr)
    five_y_pr = fof_mf_table[i].find_all('td', style="line-height: 12px; font-size: 11px!important")[6].text
    print(five_y_pr)
    # print(funds_table[i].find_all('td',style="line-height: 12px; font-size: 11px!important")[7].text)
    aum_rs_cr = fof_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; text-align:right; padding-right:30px;").text
    print(aum_rs_cr)
    one_w_pr = fof_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important;")
    print(one_w_pr.text)
    one_y_pr = fof_mf_table[i].find('td', style="line-height: 12px; font-size: 11px!important; background:#f1f0f0!important").text
    print(one_y_pr)
    csv_writer.writerow(
        [fund_name, category, aum_rs_cr, one_w_pr.text, one_m_pr, three_m_pr, six_m_pr, one_y_pr, three_y_pr,
         five_y_pr])


csv_file.close()