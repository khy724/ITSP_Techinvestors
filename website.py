from flask import Flask, request, render_template, url_for
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #fetching the data from the form field using its id
        input_age = int(request.form['age'])
        input_amount = float(request.form['amount'])
        input_profile = str(request.form['profile'])
        
        return render_template('result.html', input_age, input_amount, input_profile)




if __name__ == '__main__':
    app.run(debug=True)