from flask import Flask, request
from flask_cors import CORS, cross_origin
import joblib
import numpy as np

model = joblib.load('svm_model.pkl')

app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin()
def helloworld():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    SepalLengthCm = float(request.values.get('SepalLengthCm'))                      
    SepalWidthCm = float(request.values.get('SepalWidthCm'))
    PetalLengthCm = float(request.values.get('PetalLengthCm'))
    PetalWidthCm = float(request.values.get('PetalWidthCm'))
    data = [SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]
    print(data)
    prediction = model.predict(np.array(data).reshape(1, -1))
    return str(prediction[0])