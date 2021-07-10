import pandas as pd
import csv
# read specific columns of csv file using Pandas

df = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '1_w_pr'])
#print(df)

csv_file=open('1_w.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_w_pr'])
for i in range(0,len(df['aum_rs_cr'])):
    Fund_name = df['Fund name'][i]
    #print(Fund_name)
    category = df['category'][i]
    #print(category)
    aum_rs_cr = df['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_week_pr = df['1_w_pr'][i]
    print(one_week_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_week_pr])



one_week_sorted_df = df.sort_values(by=["1_w_pr"], ascending=False)

one_week_sorted_df.to_csv('1_week.csv', index=False)

aaf = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '1_m_pr'])
#print(df)
csv_file.close()
csv_file=open('1_m.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_m_pr'])
for i in range(0, len(aaf['aum_rs_cr'])):
    Fund_name = aaf['Fund name'][i]
    #print(Fund_name)
    category = aaf['category'][i]
    #print(category)
    aum_rs_cr = aaf['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_m_pr = aaf['1_m_pr'][i]
    #print(one_m_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



one_week_sorted_df = aaf.sort_values(by=["1_m_pr"], ascending=False)

one_week_sorted_df.to_csv('1_month.csv', index=False)

gff = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '3_m_pr'])
#print(df)
csv_file.close()
csv_file=open('3_m.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '3_m_pr'])
for i in range(0, len(gff['aum_rs_cr'])):
    Fund_name = gff['Fund name'][i]
    #print(Fund_name)
    category = gff['category'][i]
    #print(category)
    aum_rs_cr = gff['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_m_pr = gff['3_m_pr'][i]
    #print(one_m_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



one_week_sorted_df = gff.sort_values(by=["3_m_pr"], ascending=False)

one_week_sorted_df.to_csv('3_month.csv', index=False)

aaaa = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '6_m_pr'])
#print(df)
csv_file.close()
csv_file=open('6_m.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '6_m_pr'])
for i in range(0, len(aaaa['aum_rs_cr'])):
    Fund_name = aaaa['Fund name'][i]
    #print(Fund_name)
    category = aaaa['category'][i]
    #print(category)
    aum_rs_cr = aaaa['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_m_pr = aaaa['6_m_pr'][i]
    #print(one_m_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



one_week_sorted_df = aaaa.sort_values(by=["6_m_pr"], ascending=False)

one_week_sorted_df.to_csv('6_month.csv', index=False)

aaffff = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '1_y_pr'])
#print(df)
csv_file.close()
csv_file=open('1_y.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_y_pr'])
for i in range(0, len(aaffff['aum_rs_cr'])):
    Fund_name = aaffff['Fund name'][i]
    #print(Fund_name)
    category = aaffff['category'][i]
    #print(category)
    aum_rs_cr = aaffff['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_m_pr = aaffff['1_y_pr'][i]
    #print(one_m_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



one_week_sorted_df = aaffff.sort_values(by=["1_y_pr"], ascending=False)

one_week_sorted_df.to_csv('1_year.csv', index=False)

aaaaaaa = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '3_y_pr'])
#print(df)
csv_file.close()
csv_file=open('3_y.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '3_y_pr'])
for i in range(0, len(aaaaaaa['aum_rs_cr'])):
    Fund_name = aaaaaaa['Fund name'][i]
    #print(Fund_name)
    category = aaaaaaa['category'][i]
    #print(category)
    aum_rs_cr = aaaaaaa['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_m_pr = aaaaaaa['3_y_pr'][i]
    #print(one_m_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



one_week_sorted_df = aaaaaaa.sort_values(by=["3_y_pr"], ascending=False)

one_week_sorted_df.to_csv('3_year.csv', index=False)

njjw = pd.read_csv("mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '5_y_pr'])
#print(df)
csv_file.close()
csv_file=open('5_y.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '5_y_pr'])
for i in range(0, len(njjw['aum_rs_cr'])):
    Fund_name = njjw['Fund name'][i]
    #print(Fund_name)
    category = njjw['category'][i]
    #print(category)
    aum_rs_cr = njjw['aum_rs_cr'][i]
    #print(aum_rs_cr)
    one_m_pr = njjw['5_y_pr'][i]
    #print(one_m_pr)
    csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



one_week_sorted_df = njjw.sort_values(by=["5_y_pr"], ascending=False)

one_week_sorted_df.to_csv('5_year.csv', index=False)

csv_file.close()







