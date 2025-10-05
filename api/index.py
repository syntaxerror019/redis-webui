from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'demo'

@app.route('/about')
def about():
    return 'About'