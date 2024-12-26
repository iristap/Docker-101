from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/bmi', methods=['GET'])
@cross_origin()
def bmi():
    print("test")
    weight = float(request.values.get('weight'))
    height = float(request.values.get('height'))
    bmi = weight / ((height / 100) ** 2)
    return str(bmi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)