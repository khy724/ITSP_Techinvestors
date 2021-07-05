from flask import Flask, request, render_template, url_for
import pandas as pd
import numpy as np

app = Flask(__name__)

def a(inp: float):
    
    df = pd.read_csv(r"C:\Users\KHYATI PATEL\Downloads\assignment_1_data.csv")
    a = df.to_string().split()
    sat =[]
    gpa =[]
#print(df.to_string())
    for i in range(1,(len(a)+1)//3):
        sat.append(float(a[i*3]))
        gpa.append(float(a[3*i+1]))
    x = np.array(sat)
    y = np.array(gpa)
    x = x/1000
    #plt.scatter(x*1000, y)
    X = np.column_stack((np.ones(len(x)),x))
    theta = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)
    outp = theta[0]+ theta[1]*inp
    return outp

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #fetching the data from the form field using its id
        input_ = int(request.form['content'])
        output_ = a(input_)
        return render_template('index.html', out=output_)
    else:
        return render_template('index.html', out=0)



if __name__ == '__main__':
    app.run(debug=True)



