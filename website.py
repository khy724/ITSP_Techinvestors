from flask import Flask, request, render_template, url_for
import pandas as pd
import requests
import json
import numpy as np
from werkzeug.utils import redirect
import indiabonds_0_1_scrap
import indianbonds_1_3_scrap
import indianbonds_3_5_scrap
import indianbonds_5_plus_scrap
import mf_scrap
import senior_cit_fd_scrap
import fd_data_scrap
import sorted
import senior_fd_sorted
import stock_graph
import stock_5
import stock_div

app = Flask(__name__)
age = 0
amount = 0
large_cap = 0
mid_cap =0
small_cap=0
fd=0
bonds=0
mf=0
stocks=0
@app.route('/')
def func(): 
    return render_template('index.html')

@app.route('/asset/',methods=['GET','POST'])
def func1():
    if request.method =='GET':
        return render_template('asset.html')
    if request.method =='POST':
        global age
        global amount
        age = int(request.form['age'])
        
        amount = float(request.form['amount'])
        #input_profile = str(request.form['profile'])
        return redirect('/result/')
        
@app.route('/result/',methods = ['GET'])
def res():
    if request.method == 'GET':
       return render_template('result.html')

@app.route('/moderate/',methods=['GET','POST'])
def func2():
    if request.method == 'GET':
        global amount
        large_cap = amount*0.2
        mid_cap =amount*0.2
        small_cap=amount*0.1
        fd=amount*0.05
        bonds=amount*0.25
        mf=amount*0.1
        stocks=amount*0.6
        return render_template('moderate.html',am = amount)

@app.route('/very_cons/',methods=['GET','POST'])
def func3():
    if request.method == 'GET':
        global amount
        large_cap = amount*0.1
        mid_cap =amount*0.05
        small_cap=amount*0
        fd=amount*0.25
        bonds=amount*0.5
        mf=amount*0.1
        stocks=amount*0.15
        return render_template('very_cons.html',am = amount)

@app.route('/cons/',methods=['GET','POST'])
def func4():
    if request.method == 'GET':
        global amount
        large_cap = amount*0.15
        mid_cap =amount*0.1
        small_cap=amount*0.1
        fd=amount*0.1
        bonds=amount*0.4
        mf=amount*0.1
        stocks=amount*0.4
        return render_template('cons.html',am = amount)

@app.route('/agr/',methods=['GET','POST'])
def func5():
    if request.method == 'GET':
        global amount
        large_cap = amount*0.25
        mid_cap =amount*0.15
        small_cap=amount*0.15
        fd=amount*0
        bonds=amount*0.15
        mf=amount*0.15
        stocks=amount*0.7
        return render_template('agr.html',am = amount)

@app.route('/very_agr/',methods=['GET','POST'])
def func6():
    if request.method == 'GET':
        global amount
        large_cap = amount*0.2
        mid_cap =amount*0.2
        small_cap=amount*0.25
        fd=amount*0.5
        bonds=amount*0.05
        mf=amount*0.1
        stocks=amount*0.8
        return render_template('very_agr.html',am = amount)


@app.route('/bonds/',methods=['POST'])
def func8():
    if request.method =='POST':
        return render_template('bonds.html')
    
        #input_profile = str(request.form['profile'])
    return redirect('/bonds_junc/')

@app.route('/mf/',methods=['POST'])
def func9():
    if request.method =='POST':
        return render_template('mf.html')
    return redirect('/mf_junc')    

@app.route('/stocks/',methods=['POST'])
def func10():
    if request.method =='POST':
        return render_template('stocks.html')



@app.route('/bonds_junc/',methods = ['POST'])
def junc():
    if request.method == 'POST':
       return render_template('bonds_junc.html')

@app.route('/bond_0_1/',methods=['GET'])
def func12():
    if request.method =='GET':
        df = indiabonds_0_1_scrap.a()
        name,coupon,call_date,rating,type_of_bond,yeild,price = df['name'],df['coupon'],df['call_date'],df['rating'],df['type_of_bond'],df['yeild'],df['price']
        return render_template('bonds_table.html',NAME= name,COUPON= coupon,CALL_DATE=call_date,RATING=rating,TYPE_OF_BOND=type_of_bond,YEILD=yeild,PRICE=price)
       
@app.route('/bond_1_3/',methods=['GET'])
def func123():
    if request.method =='GET':
        df = indianbonds_1_3_scrap.a()
        name,coupon,call_date,rating,type_of_bond,yeild,price = df['name'],df['coupon'],df['call_date'],df['rating'],df['type_of_bond'],df['yeild'],df['price']
        return render_template('bonds_table.html',NAME= name,COUPON= coupon,CALL_DATE=call_date,RATING=rating,TYPE_OF_BOND=type_of_bond,YEILD=yeild,PRICE=price)

@app.route('/bond_3_5/',methods=['GET'])
def func124():
    if request.method =='GET':
        df = indianbonds_3_5_scrap.a()
        name,coupon,call_date,rating,type_of_bond,yeild,price = df['name'],df['coupon'],df['call_date'],df['rating'],df['type_of_bond'],df['yeild'],df['price']
        return render_template('bonds_table.html',NAME= name,COUPON= coupon,CALL_DATE=call_date,RATING=rating,TYPE_OF_BOND=type_of_bond,YEILD=yeild,PRICE=price)
@app.route('/bond_5_/',methods=['GET'])
def func125():
    if request.method =='GET':
        df = indianbonds_5_plus_scrap.a()
        name,coupon,call_date,rating,type_of_bond,yeild,price = df['name'],df['coupon'],df['call_date'],df['rating'],df['type_of_bond'],df['yeild'],df['price']

        return render_template('bonds_table.html',NAME= name,COUPON= coupon,CALL_DATE=call_date,RATING=rating,TYPE_OF_BOND=type_of_bond,YEILD=yeild,PRICE=price)
@app.route('/mf_junc/',methods = ['POST'])
def junc1():
    if request.method == 'POST':
       return render_template('mf_junc.html')

@app.route('/1_week/',methods=['GET']) 
def funca():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.a()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['1_w_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)
@app.route('/1_month/',methods=['GET']) 
def funcb():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.b()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['1_m_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)     
@app.route('/3_months/',methods=['GET']) 
def funcc():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.c()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['3_m_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)         

@app.route('/6_months/',methods=['GET']) 
def funcd():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.d()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['6_m_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)         

@app.route('/1_year/',methods=['GET']) 
def funce():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.e()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['1_y_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)         

@app.route('/3_years/',methods=['GET']) 
def funcf():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.f()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['3_y_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)         

@app.route('/5_years/',methods=['GET']) 
def funcg():
    if request.method =='GET':
        mf_scrap.a()
        df =  sorted.g()
        name,category,aum_rs_cr,one_week_pr= df['Fund name'],df['category'], df['aum_rs_cr'] , df['5_y_pr'] 
        return render_template('mf_table.html', NAME = name, CATEGORY = category, AUM_RS_CR = aum_rs_cr, PR=one_week_pr)         



@app.route('/fdrate/',methods=['POST','GET'])
def func11():
    if request.method =='GET' or 'POST':
        if age<60:
            
            '''df = fd_data_scrap.a(fd_data_scrap.a())
            df= fd_data_scrap.b(df)'''
            #df = fd_data_scrap.a()
            df = fd_data_scrap.func(fd_data_scrap.a())
            df = fd_data_scrap.b(df)

            banks,interest_rate = df['Banks'], df['interest_rate']

            return render_template('fd_table.html', BANKS= banks, INTEREST_RATE= interest_rate)
        else:
            return redirect('/sen_rates/')


@app.route('/sen_rates/',methods=['GET','POST'])
def neeshikhyati():
    if request.method =='GET':
        return render_template('sen_fd_rates.html')

@app.route('/sen_junc/',methods = ['POST'])
def func14():
    if request.method == 'POST':
       return render_template('sen_junc.html')
                 
@app.route('/less_1/',methods=['GET']) 
def func15():
    if request.method =='GET':
        df =  senior_fd_sorted.a1(senior_cit_fd_scrap.a())
        banks,interest_rate= df['fixed_dep_with_bank_name'],df['less_than_one_year']  
        return render_template('fd_table.html',BANKS=banks,INTEREST_RATE=interest_rate)    

@app.route('/1_5y/',methods=['GET']) 
def func16():
    if request.method =='GET':
        df =  senior_fd_sorted.a2(senior_cit_fd_scrap.a())
        banks,interest_rate= df['fixed_dep_with_bank_name'],df['one_to_five_year'] 
        return render_template('fd_table.html',BANKS=banks,INTEREST_RATE=interest_rate)    

@app.route('/5_y/',methods=['GET']) 
def func17():
    if request.method =='GET':
        df =  senior_fd_sorted.a3(senior_cit_fd_scrap.a())
        banks,interest_rate= df['fixed_dep_with_bank_name'],df['more_than_five'] 
        return render_template('fd_table.html',BANKS=banks,INTEREST_RATE=interest_rate)    

@app.route('/dividend/',methods=['GET','POST'])
def func18():
    if request.method =='POST':
        df = stock_div.a()
        comp,p_e,y_1_ret,prp,y_3_avg,pv,y_1_pg= df['company_name '] ,df['p/e_ratio'],df['1_yr_return_pr'],df['payout_ratio_pr'],df['3_yr_avg_div_payout'],df['prize_value'],df['1_yr_profit_growth_pr']
        return render_template('stock_table.html',COMP=comp,P_E=p_e,Y_1_RET=y_1_ret,PRP=prp,Y_3_AVG=y_3_avg,PV=pv,Y_1_PG=y_1_pg)
@app.route('/pred/',methods=['GET','POST'])
def func19():
    if request.method == 'POST':
        day=int(request.form["vol"])
        sticker = []
        lticker = []
        sticker = stock_5.a(day,small_cap)
        lticker = stock_5.b(day,large_cap)
        mticker = stock_5.c(day,mid_cap)
        array1 = stock_graph.a(sticker)
        array2 = stock_graph.a(lticker)
        array3 = stock_graph.a(mticker)
        return render_template('stock_graph.html',array1=array1,array2=array2,array3=array3,LTicker=lticker,STicker=sticker, MTicker=mticker)

''''''
''''''
if __name__ == '__main__':
    app.run(debug=True)