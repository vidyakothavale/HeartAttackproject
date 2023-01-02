import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__,template_folder='templates')
model = pickle.load(open("Rf.pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template("index.html")
@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    #return render_template("index.html", prediction_text = "The attack is {}".format(prediction))
    if prediction[0] == 0:
        prediction="Less Chance of Heart Attack.."
    else:
       prediction= "High Chance of Heart Attack.."
         
    return render_template('index.html',prediction=prediction)
    
if __name__ == "__main__":
    flask_app.run(host='0.0.0.0',port=8086)
    