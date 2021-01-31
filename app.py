from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/')
def index():
    return render_template('index.html', test="")

@app.route("/",methods = ['GET'])
def poop();
    return request.form["number"]


# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     if text != "Simply Copy and Paste Your Headline Here an Press Submit~":
#         predictionNum = int(predictor(text))
#         result = ''
#         if predictionNum == 1:
#             result = 'This source is reliable'
#         else:
#             result = 'This source is unreliable'
#         processed_text = text.upper()
#         return render_template('index.html', test=result)
#     else:
#         return render_template('index.html', test="")
=======
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})
>>>>>>> fd7c6fe8ec5fe824aa646e3db687600b330dbb5c

if __name__ == "__main__":
    app.run(debug=True)