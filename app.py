from flask import Flask, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])#this is saying upon going to the root, do the below
#originally only allows GET method (just going to the site)
#POST is when u submit user input
def hello_world():#typically returns html
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html',output="")
    else:#if it is a POST method, we want to be able to access the input in the textbox
        Sex=request.form['Sex']
        ChestPainType=request.form['ChestPainType']
        FastingBS=request.form['FastingBS']
        RestingECG=request.form['RestingECG']
        ExerciseAngina=request.form['ExerciseAngina']
        ST_Slope=request.form['ST_Slope']
        Age=request.form['Age']
        RestingBP=request.form['RestingBP']
        Cholesterol=request.form['Cholesterol']
        MaxHR=request.form['MaxHR']
        Oldpeak=request.form['Oldpeak']

        model = load('model.joblib')
        inp=np.array([int(str(Age)),int(str(RestingBP)),int(str(Cholesterol)),int(str(MaxHR)),int(str(Oldpeak))]+[0 for i in range(16)])
        feat_dict={'F':5,'M':6,'ASY':7,'ATA':8,'NAP':9,'TA':10,
        '0':11,'1':12,'LVH':13,'Normal':14,'ST':15,'N':16,'Y':17,
        'Down':18,'Flat':19,'Up':20}
        
        inp[feat_dict[str(Sex)]]=1
        inp[feat_dict[str(ChestPainType)]]=1
        inp[feat_dict[str(FastingBS)]]=1
        inp[feat_dict[str(RestingECG)]]=1
        inp[feat_dict[str(ExerciseAngina)]]=1
        inp[feat_dict[str(ST_Slope)]]=1

        res=model.predict([inp])[0]
        output=round(model.predict_proba([inp])[0][1]*100,1)
        #proba=round(model.predict_proba([inp])[0][1]*100,1)
        
        #if res == 0:
        return render_template("index.html",output=output) #'Patient is not likely to have heart failure.'
        #else:
         #  return render_template(#'Patient is likely to have heart failure (probability= '+str(proba)+ '%).'

@app.errorhandler(500)
def page_not_found(e):
    return render_template('index.html',output=500), 500

@app.errorhandler(400)
def page_not_found(e):
    return render_template('index.html',output=400), 400

if __name__ == '__main__':
    app.run(debug=True)