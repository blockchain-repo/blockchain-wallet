from flask import Flask,redirect,request,render_template,url_for,jsonify
import os
import sys
import json
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from create_config import create_config
from create_account import create_account
from account_utxo_balance import UTXO
from merge_utxo import merge_utxo
from tx_record import tx_record
from create_asset_tx import create_asset_tx
from transfer_asset_tx import transfer_asset_tx
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
# Flask自带在端口8081上监听
# 首页地址 http://localhost:8081/
# 账户表单 http://localhost:8081/account


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    account = {}
    config = {}
    balance = 0
    try:
        with open('.account') as fp:
            account = json.load(fp)
            verifying_key = account['verifying_key']
    except:
        pass
    try:
        with open('.config') as fp:
            config = json.load(fp)
            host_ip = config['host_ip']
            host_port = config['host_port']
            utxo = json.loads(UTXO(verifying_key,host_ip,host_port))
            for i in utxo:
                balance += i['amount']
    except:
        pass
    return render_template('home.html',host_conf = config,account = account,balance = balance)

@app.route('/config', methods=['GET'])
def config_form():
    return '''<form action="/config" method="post">
                <p>Host ip  :<input name="host_ip"></p>
                <p>Host port:<input name="host_port"></p>
                <p><button type="submit">create</button></p>
                </form>'''


@app.route('/config', methods=['POST'])
def config():
    # 需要从request对象读取表单内容
    if request.form['host_ip'] and request.form['host_port']:
        create_config(request.form['host_ip'],request.form['host_port'])
        return redirect(url_for('home'))
    return '<h3>Please input host ip,port</h3>'

@app.route('/account', methods=['GET'])
def account_form():
    return '''<form action="/account" method="post">
                <p>User name:</p>
                <p><input name="username"></p>
                <p><button type="submit">create</button></p>
                </form>'''


@app.route('/account', methods=['POST'])
def account():
    # 需要从request对象读取表单内容
    if request.form['username'] :
        create_account(request.form['username'])
        return redirect(url_for('home'))
    return '<h3>Please input your username</h3>'


@app.route('/utxo', methods=['GET'])
def account_utxo():
    account = {}
    try:
        with open('.account') as fp:
            account = json.load(fp)
            verifying_key = account['verifying_key']
        with open('.config') as fp:
            config = json.load(fp)
            host_ip = config['host_ip']
            host_port = config['host_port']
            utxo = json.loads(UTXO(verifying_key,host_ip,host_port))
            for u in utxo:
                u.pop('details')
            return jsonify(result = utxo)
    except:
        return jsonify({'error':'500'})

@app.route('/merge', methods=['GET'])
def merge():
    account = {}
    try:
        with open('.account') as fp:
            account = json.load(fp)
            username = account['username']
            verifying_key = account['verifying_key']
            signing_key = account['signing_key']
        with open('.config') as fp:
            config = json.load(fp)
            host_ip = config['host_ip']
            host_port = config['host_port']
            merge = merge_utxo(verifying_key,signing_key,host_ip,host_port)
            return jsonify(result = merge)
    except:
        return jsonify({'error':'500'})

@app.route('/record', methods=['GET'])
def record():
    account = {}
    try:
        with open('.account') as fp:
            account = json.load(fp)
            verifying_key = account['verifying_key']
        with open('.config') as fp:
            config = json.load(fp)
            host_ip = config['host_ip']
            host_port = config['host_port']
            record = json.loads(tx_record(verifying_key,host_ip,host_port))
            return jsonify(result = record)
    except:
        return jsonify({'error':'500'})

@app.route('/create', methods=['GET'])
def create_form():
    return '''<form action="/create" method="post">
                <p>Asset amount:</p>
                <p><input name="amount"></p>
                <p><button type="submit">create</button></p>
                </form>'''

@app.route('/create', methods=['POST'])
def create():
    # 需要从request对象读取表单内容
    if request.form['amount']:
        account = {}
        try:
            with open('.account') as fp:
                account = json.load(fp)
                signing_key = account['signing_key']
                verifying_key = account['verifying_key']
            with open('.config') as fp:
                config = json.load(fp)
                host_ip = config['host_ip']
                host_port = config['host_port']
                create = create_asset_tx(verifying_key,signing_key,int(request.form['amount']),host_ip,host_port)
            return jsonify(result = create)
        except:
            return jsonify({'error':'500'})

@app.route('/transfer', methods=['GET'])
def transfer_form():
    return '''<form action="/transfer" method="post">
                <p>Owner after :<input name="after"></p>
                <p>Amount      :<input name="amount"></p>
                <p><button type="submit">transfer</button></p>
                </form>'''

@app.route('/transfer', methods=['POST'])
def transfer():
    # 需要从request对象读取表单内容
    if request.form['amount'] and request.form['after']:
        account = {}
        try:
            with open('.account') as fp:
                account = json.load(fp)
                signing_key = account['signing_key']
                verifying_key = account['verifying_key']
            with open('.config') as fp:
                config = json.load(fp)
                host_ip = config['host_ip']
                host_port = config['host_port']
                transfer = transfer_asset_tx(verifying_key,signing_key,request.form['after'],int(request.form['amount']),host_ip,host_port)
            return jsonify(result = transfer)
        except:
            raise
            return jsonify({'error':'500'})


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8081)

