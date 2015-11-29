__author__ = 'aaronmsmith'
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello, World. I''m flasky!'