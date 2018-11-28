# coding: utf-8
from flask import Flask
from flask import request, jsonify, g, render_template


app = Flask(__name__)


@app.route('/chat/')
def health_check():
    return jsonify({'code':200, 'data':'welcome'})


@app.route('/private/', methods=['POST','GET'])
def get_rsa_url():
    if request.form.get('kw') == '110':
        return jsonify({'code': 200, 'data': '123456789'})
    else:
        return jsonify({'code': 200, 'data':'www.baidu.com'})


@app.route('/chatroom/<token>', methods=['GET'])
def chat(token):
    print(token)
    if token == '123':
        return render_template('./chat.html')
    else:
        return render_template('./error.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

