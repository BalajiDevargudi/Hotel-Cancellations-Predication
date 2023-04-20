from flask import Flask,render_template, url_for,request, jsonify
import pickle, numpy, pandas, random, scipy, 



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

@app.route('/predict1',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output1 = round(prediction[0], 2)

    return render_template('index1.html', prediction_text1='Employee Salary should be $ {}'.format(output1))

if __name__=="__main__":
    app.run(debug=True)
