from flask import Flask,render_template, url_for,request
import random


app=Flask(__name__)


@app.route('/')
def home():

    
    return render_template('index.html')


@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
       mylist = ["Is Cancelled", "Is Not Cancelled"]
       output = random.sample(mylist, k=1)
       if request.method == 'POST':  
        result = request.form  
       return render_template("result_data.html", result = result, prediction_text='The Hotel Booking : {}'.format(output))  


if __name__=="__main__":
    app.run(debug=True)