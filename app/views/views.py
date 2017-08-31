import json
import time

from flask import render_template, request

import config as c
from app import app
from app.models.account_utxo_balance import UTXO
from app.models.create_asset_tx import create_asset_tx
from app.models.query_tx import query_tx
from app.models.secretbox import open_secretbox
from app.models.transfer_asset_tx import transfer_asset_tx
from app.models.tx_record import tx_record, format_time

public = c.config['keypair']['public']
private = c.config['keypair']['private']
host = c.config['server']['host']
port = c.config['server']['port']


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    balance = 0
    utxo = json.loads(UTXO(public, host, port))
    for i in utxo['data']:
        balance += i['amount']
    return render_template('index.html', config=c.config, balance=balance)


@app.route('/recharge', methods=['GET'])
def recharge_get():
    balance = 0
    return render_template('recharge.html', config=c.config, balance=balance)


@app.route('/recharge', methods=['POST'])
def recharge_post():
    balance = 0
    if request.form['btc_amount'] and request.form['target'] and request.form['private_flag']:
        amount = int(request.form['btc_amount'])
        target = request.form['target']
        flag = True if request.form['private_flag'] == "true" else False
        msg = request.form.get('leave_message', '')
        create_asset_tx(public, private, target, amount, msg, flag, host, port)
        time.sleep(2)
    utxo = json.loads(UTXO(public, host, port))
    for i in utxo['data']:
        balance += i['amount']
    return render_template('index.html', config=c.config, balance=balance)


@app.route('/transfer', methods=['GET'])
def transfer_get():
    balance = 0
    return render_template('transfer.html', config=c.config, balance=balance)


@app.route('/transfer', methods=['POST'])
def transfer_post():
    balance = 0
    if request.form['btc_amount'] and request.form['target'] and request.form['private_flag']:
        amount = int(request.form['btc_amount'])
        target = request.form['target']
        flag = True if request.form['private_flag'] == "true" else False
        msg = request.form.get('leave_message', '')
        transfer_asset_tx(public, private, target, amount, msg, flag, host, port)
        time.sleep(2)
    utxo = json.loads(UTXO(public, host, port))
    for i in utxo['data']:
        balance += i['amount']
    return render_template('index.html', config=c.config, balance=balance)


@app.route('/transactions', methods=['GET'])
def transactions_get():
    balance = 0
    txs = json.loads(tx_record(public, host, port))
    for tx in txs:
        tx['timestamp'] = format_time(tx['timestamp'])
        if tx['operation'] == "CREATE":
            tx['operation'] = "充值"
        else:
            tx['operation'] = "转出" if tx['owner_before'] == public else "转入"
    return render_template('transactions.html', config=c.config, balance=balance, txs=txs)


@app.route('/query', methods=['GET'])
def query_get():
    balance = 0
    return render_template('query.html', config=c.config, balance=balance)


@app.route('/query', methods=['POST'])
def query_post():
    balance = 0
    tx = {}
    msg = ""
    if request.form['target']:
        tx = json.loads(query_tx(request.form['target'], host, port)).get('data', {})
        data = tx['transaction']['metadata']['data']
        if data.get('raw', ''):
            msg = data['raw']
        elif data.get('encrypted', '') and data.get('nonce', ''):
            msg = open_secretbox(private, data['encrypted'], data['nonce']).decode()
    return render_template('query.html', config=c.config, balance=balance, tx=tx, msg=msg)

# @app.route('/config', methods=['GET'])
# def config_form():
#     return '''<form action="/config" method="post">
#                 <p>Host ip  :<input name="host_ip"></p>
#                 <p>Host port:<input name="host_port"></p>
#                 <p><button type="submit">create</button></p>
#                 </form>'''
#
#
# @app.route('/config', methods=['POST'])
# def config():
#     # 需要从request对象读取表单内容
#     if request.form['host_ip'] and request.form['host_port']:
#         create_config(request.form['host_ip'], request.form['host_port'])
#         return redirect(url_for('home'))
#     return '<h3>Please input host ip,port</h3>'
#
#
# @app.route('/account', methods=['GET'])
# def account_form():
#     return '''<form action="/account" method="post">
#                 <p>User name:</p>
#                 <p><input name="username"></p>
#                 <p><button type="submit">create</button></p>
#                 </form>'''
#
#
# @app.route('/account', methods=['POST'])
# def account():
#     # 需要从request对象读取表单内容
#     if request.form['username']:
#         create_account(request.form['username'])
#         return redirect(url_for('home'))
#     return '<h3>Please input your username</h3>'
#
#
# @app.route('/utxo', methods=['GET'])
# def account_utxo():
#     account = {}
#     try:
#         with open('.account') as fp:
#             account = json.load(fp)
#             verifying_key = account['verifying_key']
#         with open('.config') as fp:
#             config = json.load(fp)
#             host_ip = config['host_ip']
#             host_port = config['host_port']
#             utxo = json.loads(UTXO(verifying_key, host_ip, host_port))
#             print(utxo)
#             for u in utxo['data']:
#                 u.pop('details')
#             return jsonify(result=utxo)
#     except:
#         return jsonify({'error': '500'})
#
#
# @app.route('/merge', methods=['GET'])
# def merge():
#     account = {}
#     try:
#         with open('.account') as fp:
#             account = json.load(fp)
#             username = account['username']
#             verifying_key = account['verifying_key']
#             signing_key = account['signing_key']
#         with open('.config') as fp:
#             config = json.load(fp)
#             host_ip = config['host_ip']
#             host_port = config['host_port']
#             merge = merge_utxo(verifying_key, signing_key, host_ip, host_port)
#             return jsonify(result=merge)
#     except:
#         return jsonify({'error': '500'})
#
#
# @app.route('/record', methods=['GET'])
# def record():
#     account = {}
#     try:
#         with open('.account') as fp:
#             account = json.load(fp)
#             verifying_key = account['verifying_key']
#         with open('.config') as fp:
#             config = json.load(fp)
#             host_ip = config['host_ip']
#             host_port = config['host_port']
#             record = json.loads(tx_record(verifying_key, host_ip, host_port))
#             return jsonify(result=record)
#     except:
#         return jsonify({'error': '500'})
#
#
# @app.route('/create', methods=['GET'])
# def create_form():
#     return '''<form action="/create" method="post">
#                 <p>Asset amount:</p>
#                 <p><input name="amount"></p>
#                 <p><button type="submit">create</button></p>
#                 </form>'''
#
#
# @app.route('/create', methods=['POST'])
# def create():
#     # 需要从request对象读取表单内容
#     if request.form['amount']:
#         account = {}
#         try:
#             with open('.account') as fp:
#                 account = json.load(fp)
#                 signing_key = account['signing_key']
#                 verifying_key = account['verifying_key']
#             with open('.config') as fp:
#                 config = json.load(fp)
#                 host_ip = config['host_ip']
#                 host_port = config['host_port']
#                 create = create_asset_tx(verifying_key, signing_key, int(request.form['amount']), host_ip, host_port)
#             return jsonify(result=create)
#         except:
#             return jsonify({'error': '500'})
#
#
# @app.route('/transfer', methods=['GET'])
# def transfer_form():
#     return '''<form action="/transfer" method="post">
#                 <p>Owner after :<input name="after"></p>
#                 <p>Amount      :<input name="amount"></p>
#                 <p><button type="submit">transfer</button></p>
#                 </form>'''
#
#
# @app.route('/transfer', methods=['POST'])
# def transfer():
#     # 需要从request对象读取表单内容
#     if request.form['amount'] and request.form['after']:
#         account = {}
#         try:
#             with open('.account') as fp:
#                 account = json.load(fp)
#                 signing_key = account['signing_key']
#                 verifying_key = account['verifying_key']
#             with open('.config') as fp:
#                 config = json.load(fp)
#                 host_ip = config['host_ip']
#                 host_port = config['host_port']
#                 transfer = transfer_asset_tx(verifying_key, signing_key, request.form['after'],
#                                              int(request.form['amount']), host_ip, host_port)
#             return jsonify(result=transfer)
#         except:
#             return jsonify({'error': '500'})
