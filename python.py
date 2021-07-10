#%%
import csv
file = open("mutual_funds.csv")
csvreader = csv.reader(file)
for x in csvreader:
    print(x)
