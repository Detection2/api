import numpy as np
from flask import Flask, request, jsonify
import pickle

model = pickle.load(open(r'C:\Users\ADMIN\PycharmProjects\Malephas-API\model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    # bytes_data.encode('utf-8')

    atsign_in_URLs = request.form['atsign_in_URLs']
    Attachments = request.form['Attachments']
    Css = request.form['Css']
    Html_content = request.form['Html_content']
    IPs_in_URLs = request.form['IPs_in_URLs']
    URLs = request.form['URLs']

    var1 = int(atsign_in_URLs.encode('utf-8'))
    var2 = int(Attachments.encode('utf-8'))
    var3 = int(Css.encode('utf-8'))
    var4 = int(Html_content.encode('utf-8'))
    var5 = int(IPs_in_URLs.encode('utf-8'))
    var6 = int(URLs.encode('utf-8'))

    input_query = np.array([[var1, var2, var3, var4, var5, var6]])

    result = model.predict(input_query)[0]

    return jsonify({'Malicious Email DETECTED': str(result)})


if __name__ == '__main__':
    app.run(debug=True)
