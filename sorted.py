import pandas as pd
import csv
# read specific columns of csv file using Pandas
#dividing the data of each timeperiod into different csv files
def a():
    df = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '1_w_pr'])

    csv_file=open('csv/1_w.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_w_pr'])
    for i in range(0,len(df['aum_rs_cr'])):
        Fund_name = df['Fund name'][i]
        category = df['category'][i]
        aum_rs_cr = df['aum_rs_cr'][i]
        one_week_pr = df['1_w_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_week_pr])
    one_week_sorted_df = df.sort_values(by=["1_w_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/1_w.csv', index=False)

    
    
    
    csv_file.close()
    xtc = pd.read_csv('csv/1_w.csv')
    
    return xtc 



def b():
    aaf = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '1_m_pr'])

    
    csv_file=open('csv/1_m.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_m_pr'])
    for i in range(0, len(aaf['aum_rs_cr'])):
        Fund_name = aaf['Fund name'][i]
        category = aaf['category'][i]
        aum_rs_cr = aaf['aum_rs_cr'][i]
        one_m_pr = aaf['1_m_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])

    one_week_sorted_df = aaf.sort_values(by=["1_m_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/1_m.csv', index=False)
    csv_file.close()
    return one_week_sorted_df

def c():
    gff = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '3_m_pr'])
   
    csv_file=open('csv/3_m.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '3_m_pr'])
    for i in range(0, len(gff['aum_rs_cr'])):
        Fund_name = gff['Fund name'][i]
        category = gff['category'][i]
        aum_rs_cr = gff['aum_rs_cr'][i]
        one_m_pr = gff['3_m_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



    one_week_sorted_df = gff.sort_values(by=["3_m_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/3_m.csv', index=False)
    csv_file.close()
    return one_week_sorted_df
def d():
    aaaa = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '6_m_pr'])
  
    csv_file=open('csv/6_m.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '6_m_pr'])
    for i in range(0, len(aaaa['aum_rs_cr'])):
        Fund_name = aaaa['Fund name'][i]
        category = aaaa['category'][i]
        aum_rs_cr = aaaa['aum_rs_cr'][i]
        one_m_pr = aaaa['6_m_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



    one_week_sorted_df = aaaa.sort_values(by=["6_m_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/6_m.csv', index=False)
    csv_file.close()
    return one_week_sorted_df
def e():
    aaffff = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '1_y_pr'])


    csv_file=open('csv/1_y.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '1_y_pr'])
    for i in range(0, len(aaffff['aum_rs_cr'])):
        Fund_name = aaffff['Fund name'][i]
        category = aaffff['category'][i]
        aum_rs_cr = aaffff['aum_rs_cr'][i]
        one_m_pr = aaffff['1_y_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



    one_week_sorted_df = aaffff.sort_values(by=["1_y_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/1_y.csv', index=False)
    csv_file.close()
    return one_week_sorted_df
def f():
    aaaaaaa = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '3_y_pr'])
   
    csv_file=open('csv/3_y.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '3_y_pr'])
    for i in range(0, len(aaaaaaa['aum_rs_cr'])):
        Fund_name = aaaaaaa['Fund name'][i]
        category = aaaaaaa['category'][i]
        aum_rs_cr = aaaaaaa['aum_rs_cr'][i]
        one_m_pr = aaaaaaa['3_y_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



    one_week_sorted_df = aaaaaaa.sort_values(by=["3_y_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/3_y.csv', index=False)
    csv_file.close()
    return one_week_sorted_df
def g():
    njjw = pd.read_csv("csv/mutual_funds.csv", usecols=['Fund name', 'category', 'aum_rs_cr', '5_y_pr'])
    
    csv_file=open('csv/5_y.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Fund name', 'category', 'aum_rs_cr', '5_y_pr'])
    for i in range(0, len(njjw['aum_rs_cr'])):
        Fund_name = njjw['Fund name'][i]
        category = njjw['category'][i]
        aum_rs_cr = njjw['aum_rs_cr'][i]
        one_m_pr = njjw['5_y_pr'][i]
        csv_writer.writerow([Fund_name,category,aum_rs_cr,one_m_pr])



    one_week_sorted_df = njjw.sort_values(by=["5_y_pr"], ascending=False)

    one_week_sorted_df.to_csv('csv/5_y.csv', index=False)
    csv_file.close()
    return one_week_sorted_df