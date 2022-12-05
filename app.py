from flask import Flask,render_template,request,jsonify
from sklearn.neighbors import KNeighborsClassifier
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    title = "Pagina de Inicio"
    return render_template("index.html",title=title)
 
@app.route('/predecir',methods=['POST'])
def predecir():
    inputs = {
        'SepalLengthCm':[request.form.get('SepalLengthCm')],
        'SepalWidthCm':[request.form.get('SepalWidthCm')],
        'PetalLengthCm':[request.form.get('PetalLengthCm')],
        'PetalWidthCm':[request.form.get('PetalWidthCm')],
    }
    i = pd.DataFrame(inputs)
    clf = joblib.load('Modelo_iris.joblib')
    r = clf.predict(i)
    title = "Pagina de Prediccion"
    return render_template("predic.html",title=title,re='',p=str(r[0]))

@app.route('/predecir2',methods=['POST'])
def predecir2():
    inputs = {
        'RM':[request.form.get('RM')],
        'LSTAT':[request.form.get('LSTAT')],
        'PTRATIO':[request.form.get('PTRATIO')],
    }
    i = pd.DataFrame(inputs)
    re = joblib.load('Modelo_casa_precio.joblib')
    r = re.predict(i)
    title = "Pagina de Prediccion"
    return render_template("predic.html",title=title,p='',re=str(r[0]))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)