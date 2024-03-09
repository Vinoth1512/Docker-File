## Flask app fro hello world 
from flask import Flask
import os

app =  Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return "Welcome to the website"

@app.route('/hello')
def hello():
    return "Hi there"

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port = 1000)