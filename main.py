from flask import Flask, render_template, request, redirect, url_for, session  # type: ignore
import pymongo  # type: ignore
import os
import certifi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)