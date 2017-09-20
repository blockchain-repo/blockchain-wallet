import json
import time

import config as c
from app import app
from app.models.account_utxo_balance import UTXO
from app.models.create_asset_tx import create_asset_tx
from app.models.query_tx import query_tx
from app.models.secretbox import open_secretbox
from app.models.transfer_asset_tx import transfer_asset_tx
from app.models.tx_record import tx_record, format_time

from flask import render_template, request, jsonify, make_response, abort

public = c.config['keypair']['public']
private = c.config['keypair']['private']
host = c.config['server']['host']
port = c.config['server']['port']
delay = 3


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
        time.sleep(delay)
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
        time.sleep(delay)
    utxo = json.loads(UTXO(public, host, port))
    for i in utxo['data']:
        balance += i['amount']
    return render_template('index.html', config=c.config, balance=balance)


@app.route('/transactions', methods=['GET'])
def transactions_get():
    balance = 0
    txs = json.loads(tx_record(public, host, port))['record']
    for tx in txs:
        tx['timestamp'] = format_time(tx['timestamp'])
        if tx['operation'] == "CREATE":
            tx['operation'] = "充值"
            tx['target'] = ""
        elif tx['owner_before'] == public and tx['owners_after'] == public:
            tx['operation'] = "自转"
            tx['target'] = ""
        elif tx['owner_before'] == public:
            tx['operation'] = "转出"
            tx['target'] = tx['owners_after']
        elif tx['owners_after'] == public:
            tx['operation'] = "转入"
            tx['target'] = tx['owner_before']
        else:
            tx['operation'] = "未知"
            tx['target'] = ""
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


@app.route('/transaction', methods=['GET'])
def transaction_get():
    if request.args.get('tx_id'):
        tx = json.loads(query_tx(request.args.get('tx_id'), host, port)).get('data', {})
        return jsonify(tx)
    else:
        abort(404)


@app.route('/downtx', methods=['GET'])
def downtx():
    if request.args.get('tx_id'):
        tx = json.loads(query_tx(request.args.get('tx_id'), host, port)).get('data', {})
        response = make_response(json.dumps(tx, indent=4))
        response.headers["Content-Disposition"] = "attachment; filename={}.json".format(request.args.get('tx_id'))
        return response
    else:
        abort(404)
