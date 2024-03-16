from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
#from sklearn.tree import DecisionTreeRegressor

application  = Flask(__name__)
app = application

## import pkl file----------------->>>>>>>>>
regress_model = pickle.load(open("regress2.pkl","rb"))
standard_scaler = pickle.load(open("scaler2.pkl","rb"))


## Route for home page ---------->>>>>>>>>>>
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="POST":
         PassengerId = float(request.form.get("PassengerId"))
         Pclass= float(request.form.get("Pclass"))
         Age = float(request.form.get("Age"))
         SibSp = float(request.form.get("SibSp"))
         Parch = float(request.form.get("Parch"))
         Fare = float(request.form.get("Fare"))
         Sex_female= float(request.form.get("Sex_female"))
         Sex_male = float(request.form.get("Sex_male"))
         Embarked_C = float(request.form.get("Embarked_C"))
         Embarked_Q = float(request.form.get("Embarked_Q"))
         Embarked_S = float(request.form.get("Embarked_S"))
         
         

         new_data_scaled = standard_scaler.transform([[PassengerId,Pclass,Age,SibSp,Parch,Fare,Sex_female,Sex_male,Embarked_C,Embarked_Q,Embarked_S]])
         result = regress_model.predict(new_data_scaled)

         return render_template("home.html",result=result[0])

    else:
        return render_template("home.html")
    
     





if __name__=="__main__":
    app.run(debug=True)

