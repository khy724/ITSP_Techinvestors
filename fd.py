from flask import Flask,request, render_template, url_for, redirect
import random
import pandas as pd
import csv
import fd_data_scrap
import senior_cit_fd_scrap

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect('/fd_table/') 
    


    
@app.route('/fd_table/', methods=['GET', 'POST'])
def table():
    if request.method == 'GET':
        if 'age' in session:
            age = session['age']
            if age>60:
                df = senior_cit_fd_scrap.a()
                bn,lty,otf,mtf = df['fixed_dep_with_bank_name'], df['less_than_one_year'],df['one_to_five_year'],df['more_than_five']
                return render_template('fd_table.html',BN=bn,LTY= lty,OTF= otf,MTFmtf)
            else:
                df = fd_data_scrap.a()
        Sr, List = df['sr no.'], df['list']

        return render_template('fd_table.html', SR = Sr, LIST = List) 
    else:
        return 'That did not work!'
        


if __name__ == '__main__':
    app.run(debug=True)