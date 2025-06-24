from flask import Flask, render_template, request, redirect, url_for
import os
print("FILES IN CURRENT DIR:", os.listdir())
print("FILES IN /templates:", os.listdir("templates"))


app = Flask(__name__)
accounts = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        accounts[name] = {
            'balance': amount,
            'transactions': [("Deposit", amount)]
        }
        return redirect(url_for('home'))
    return render_template('create.html')

@app.route('/balance', methods=['GET', 'POST'])
def balance():
    if request.method == 'POST':
        name = request.form['name']
        acc = accounts.get(name)
        if acc:
            return render_template('balance.html', name=name, balance=acc['balance'])
        else:
            return "Account not found", 404
    return render_template('balance.html')

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if request.method == 'POST':
        name = request.form['name']
        action = request.form['action']
        amount = float(request.form['amount'])

        acc = accounts.get(name)
        if not acc:
            return "Account not found", 404

        if action == 'deposit':
            acc['balance'] += amount
            acc['transactions'].append(("Deposit", amount))
        elif action == 'withdraw':
            if amount > acc['balance']:
                return "Insufficient balance", 400
            acc['balance'] -= amount
            acc['transactions'].append(("Withdraw", amount))
        return redirect(url_for('home'))
    return render_template('transaction.html')

@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'POST':
        name = request.form['name']
        acc = accounts.get(name)
        if not acc:
            return "Account not found", 404
        return render_template('history.html', name=name, transactions=acc['transactions'])
    return render_template('history.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
