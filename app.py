from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
db.init_app(app)

class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    account_type = db.Column(db.String(25), nullable=False)
    account_balance = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Account %r>' % self.id
    
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method =='POST':
        account = BankAccount(
            first_name = request.form['first_name'],
            last_name = request.form['last_name'],
            email = request.form['email'],
            account_type = request.form['account_type'],
            account_balance = request.form['account_balance'],
            )
        
        try:
            db.session.add(account)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the account'    
    else:
        accounts = BankAccount.query.order_by(BankAccount.id).all()
        return render_template('index.html', accounts=accounts)

@app.route('/delete/<int:id>')
def delete(id):
    account_to_delete = BankAccount.query.get_or_404(id)

    try:
        db.session.delete(account_to_delete)
        db.session.commit()
        return redirect('/') 
    except:
        return 'There was a problem deleting that account'
 
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    account = BankAccount.query.get_or_404(id)

    if request.method == 'POST':
        account = BankAccount(
            id = request.form['id'],
            first_name = request.form['first_name'],
            last_name = request.form['last_name'],
            email = request.form['email'],
            account_type = request.form['account_type'],
            account_balance = request.form['account_balance'],
        )

        try:
            db.session.merge(account)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an issue updating the account'
    else:
        return render_template('update.html', account = account)


if __name__ == "__main__":
    app.run(debug=True)