from flask import Flask, request
from flask_cors import CORS
from flask import render_template
from flask import jsonify
import subprocess

app = Flask('AIService', static_url_path='/')
CORS(app)
PORT=5555

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/get_prediction')
def predict():
    result = subprocess.run(['sh', './runProject.sh'], stdout=subprocess.PIPE)
    response = result.stdout.decode('utf-8').strip('\n');
    return jsonify(response);

app.run(debug=True, port=PORT)
