# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:05:53 2020

@author: Bharti Arora
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/<string:name>")
def index(name):
    return f"hello,World! of {name}"

@app.route("/hello")
def indexTest():
    return render_template("aboutMe.html")



if __name__ == '__main__':
    app.trace = True
    app.run()

