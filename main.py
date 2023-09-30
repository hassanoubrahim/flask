from flask import Flask, render_template, request, jsonify
from getPrediction import predModel



app = Flask(__name__)

@app.route('/')
def main():
    return "welcome! <br> application 1 :  <a href='app1/predict'> click here </a>"

@app.route('/app1/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        data = request.form
        result =  predModel(data)
    else:
        result = 0.5
        data = None
    return render_template('home.html', data = data, res = result)


if __name__ == '__main__':
    app.run(debug=True)

