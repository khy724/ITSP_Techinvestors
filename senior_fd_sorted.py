import csv
from numpy import i0
import pandas as pd

def a1(df):

    csv_file=open('csv/less_than_one_year_senior.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['fixed_dep_with_bank_name','less_than_one_year'])
    #writing row headings

    for i in range(0,len(df['fixed_dep_with_bank_name'])):
        fixed_dep_with_bank_name = df['fixed_dep_with_bank_name'][i]
        #reading data from file and storing it into  a variable
        duration= list(df['less_than_one_year'][i].split())
        #spliting the element
        min= float(duration[0])
        max= float(duration[1])
        average = (min+max)/2
        #storing this into a variables to find the average

        csv_writer.writerow([fixed_dep_with_bank_name,average])
        #making a new csv and write this into the rows created
        

    csv_file.close()
    xtc = pd.read_csv('csv/less_than_one_year_senior.csv')

    sorted = xtc.sort_values(by=["less_than_one_year"], ascending=False)
    #sorting this on the column
    sorted.to_csv('csv/less_than_one_year_senior.csv', index=False)
    xtc = pd.read_csv('csv/less_than_one_year_senior.csv')
    return xtc
def a2(df):

    csv_file=open('csv/one_to_five_year_senior.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['fixed_dep_with_bank_name','one_to_five_year'])

    for i in range(0,len(df['fixed_dep_with_bank_name'])):
        fixed_dep_with_bank_name = df['fixed_dep_with_bank_name'][i]
    #print(Fund_name)
        duration= list(df['one_to_five_year'][i].split())
        #print(duration)
        min= float(duration[0])
        max= float(duration[1])
        average = (min+max)/2

        csv_writer.writerow([fixed_dep_with_bank_name,average])
        
            
            





    csv_file.close()
    xtc = pd.read_csv('csv/one_to_five_year_senior.csv')

    sorted = xtc.sort_values(by=["one_to_five_year"], ascending=False)
    sorted.to_csv('csv/one_to_five_year_senior.csv', index=False)
    xtc = pd.read_csv('csv/one_to_five_year_senior.csv')
    return xtc




def a3(df):
    #df = pd.read_csv("senior_cit_fd_1.csv", usecols=['fixed_dep_with_bank_name','more_than_five'])
    #print(df)

    csv_file=open('csv/more_than_five_senior.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['fixed_dep_with_bank_name','more_than_five'])

    for i in range(0,len(df['fixed_dep_with_bank_name'])):
        fixed_dep_with_bank_name = df['fixed_dep_with_bank_name'][i]
    #print(Fund_name)
        duration = df['more_than_five'][i]
        #print(duration)
        
    #storing variables that we need
        csv_writer.writerow([fixed_dep_with_bank_name,duration])
        
            
            





    csv_file.close()
    xtc = pd.read_csv('csv/more_than_five_senior.csv')

    sorted = xtc.sort_values(by=["more_than_five"], ascending=False)
    #sorting data on the column more than five
    sorted.to_csv('csv/more_than_five_senior.csv', index=False)
    xtc = pd.read_csv('csv/more_than_five_senior.csv')
    return xtc


    

#return xyz






