from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib
model=joblib.load(open('hert.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def get_prediction():
    data1=request.form['data1']
    data2=request.form['data2']
    data3=request.form['data3']
    data4=request.form['data4']
    data5=request.form['data5']
    data6=request.form['data6']
    data7=request.form['data7']
    data8=request.form['data8']
    data9=request.form['data9']
    data10=request.form['data10']
    data11=request.form['data11']
    data12=request.form['data12']
    data13=request.form['data13']
    data=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]])
    predict=model.predict(data)
    return render_template('result.html',prediction=predict)
    
if __name__=='__main__':
    app.run(debug=True)