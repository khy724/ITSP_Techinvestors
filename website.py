from flask import Flask, request, render_template, url_for
import pandas as pd
import numpy as np
from werkzeug.utils import redirect
import indiabonds_0_1_scrap
import indianbonds_1_3_scrap
import indianbonds_3_5_scrap
import indianbonds_5_plus_scrap
import mf_scrap
import senior_cit_fd_scrap
import fd_data_scrap

app = Flask(__name__)
age = 0
@app.route('/')
def func():
    return render_template('index.html')

@app.route('/asset/',methods=['GET','POST'])
def func1():
    if request.method =='GET':
        return render_template('asset.html')
    if request.method =='POST':
        global age
        input_age = int(request.form['age'])
        age = input_age
        input_amount = float(request.form['amount'])
        #input_profile = str(request.form['profile'])
        return redirect('/result/')
        
@app.route('/result/',methods = ['GET'])
def res():
    if request.method == 'GET':
       return render_template('result.html')

@app.route('/moderate/',methods=['GET','POST'])
def func2():
    if request.method == 'GET':
        return render_template('moderate.html')

@app.route('/very_cons/',methods=['GET','POST'])
def func3():
    if request.method == 'GET':
        return render_template('very_cons.html')

@app.route('/cons/',methods=['GET','POST'])
def func4():
    if request.method == 'GET':
        return render_template('cons.html')

@app.route('/agr/',methods=['GET','POST'])
def func5():
    if request.method == 'GET':
        return render_template('agr.html')

@app.route('/very_agr/',methods=['GET','POST'])
def func6():
    if request.method == 'GET':
        return render_template('very_agr.html')

@app.route('/fd/',methods=['POST'])
def func7():
    if request.method =='POST':
        return render_template('fd.html')

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

@app.route('/stocks/',methods=['POST'])
def func10():
    if request.method =='POST':
        return render_template('stocks.html')

@app.route('/fdrate/',methods=['POST','GET'])
def func11():
    if request.method =='POST':
        if age<60:
            return render_template('fd_table.html')
        else:
            return render_template('sen_fd_rates.html')

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


    
'''@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #fetching the data from the form field using its id
        input_age = int(request.form['age'])
        input_amount = float(request.form['amount'])
        input_profile = str(request.form['profile'])
        
        return render_template('result.html', input_age, input_amount, input_profile)'''




if __name__ == '__main__':
    app.run(debug=True)