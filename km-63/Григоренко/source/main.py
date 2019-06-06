
import numpy as np
import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/Doc', methods=['GET'])
def Doc():
    return render_template('Student.html')


@app.route('/Branch', methods=['GET'])
def Branch():
    return render_template('File.html')


@app.route('/Change', methods=['GET'])
def Change():
    return render_template('Mark.html')


@app.route('/Search', methods=['GET'])
def Search():
    return render_template('Search.html')


if __name__ == '__main__':
    app.run(debug=True)
