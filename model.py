from flask import Flask,redirect,url_for,render_template,request
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
app=Flask(__name__)
model = pickle.load(open("loan-final-new_model.pkl", "rb"))
@app.route('/')
def welcome():
    return render_template("acc.html")
@app.route('/t',methods=['GET','POST'])
def predict():
     if request.method=="POST":
         income_a=request.form['income']
         income_c=request.form['C-income']
         Lone_amount=int(request.form['Loan-Amount'])
         Lone_term=int(request.form['Loan-term'])
         Dependent=int(request.form['Dependents'])
         if(Dependent>3):
             Dependent=3
         Property_Area=request.form['Property-Area']
         Marital_status=request.form['Marital_status']
         Self_Employed=request.form['Self-Employed']
         Education=request.form['Education']
         Gender=request.form['Gender']
         p_loan=request.form['p-loan']
         if(Property_Area=='Urban'):
             Property=1
         if(Property_Area=='Rular'):
             Property=2
         if(Property_Area=='Semi-urban'):
             Property=0
         if(Marital_status=='Single'):
             Marital=0
         if(Marital_status=='Married'):
             Marital=1
         if(Self_Employed=='yes'):
             s_employ=1
         if(Self_Employed=='No'):
             s_employ=0
         if(p_loan=='yes'):
             p_loans=1
         if(p_loan=='no'):
             p_loans=0   
         if(Education=='Graduate'):
             edu=1 
         if(Education=='Not-Graduate'):
             edu=0
         if(Gender=='Male'):
            gen=1
         if(Gender=='Female'):
            gen=0
         pred=model.predict([[
              gen,
              Marital,
              Dependent,
              edu,
              s_employ,
              income_a,
              income_c,
              Lone_amount,
              Lone_term,
              p_loans,
              Property     
         ]])      
                      
         if(str(pred[0])=='Y'):
            return render_template('succes.html',prediction_text="Congo you are eligible for loan")
         else:
            return render_template('fail.html',prediction_text="Sorry We can't Process your loan")
     return render_template("acc.html")                      
        
         
if __name__=='__main__':
    app.run(debug=True)     
    
    
    
                