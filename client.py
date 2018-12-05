# coding: utf-8
import time
from flask import Flask
from flask import request, jsonify, g, render_template,redirect,url_for
from config import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check/', methods=['POST','GET'])
def check():
    if request.form.get('kw') == '@123456':
        return render_template('recheck.html')
    else:
        return redirect(url_for('index'))


@app.route('/recheck/',methods=['POST'])
def recheck():
    if request.form.get('ps') == 'hi':
        return redirect('/chatroom/123')
    else:
        return redirect(url_for('check'))


@app.route('/chatroom/<token>', methods=['GET'])
def chat(token):
    print(token)
    if token == '123':

        messages = [{'title': 'lilei', 'content':'hello world', 'timestamp':'2018-10-12 12:25'}]

        return render_template('chat.html',messages=messages)
    else:
        return render_template('error.html')


@app.route('/new_message/', methods=['GET', 'POST'])
def new_message():
    print(request.method)
    if request.method == 'GET':
        return jsonify({'code':200,'data':'这是新消息'})
    elif request.method == 'POST':
        message = request.form.get('message')
        timestamp = time.time()
        print(message)
        return redirect('/chatroom/123')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)

