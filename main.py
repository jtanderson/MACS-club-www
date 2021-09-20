from flask import Flask,jsonify,render_template
import os
import yaml

app = Flask(__name__)

@app.context_processor
def inject_global_vars():
    return {}

@app.route('/')
def index():
    with open('data.yaml', 'r') as file:
        data = yaml.safe_load(file)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
