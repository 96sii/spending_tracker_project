from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository




transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.add_total()
    return render_template("/transactions/index.html", transactions=transactions, total=total)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    categories = category_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", categories=categories, merchants=merchants)

@transactions_blueprint.route("/transactions", methods=['POST'])
def add_transaction():
    merchant_id = request.form['merchant_id']
    amount = request.form['amount']
    date = request.form['date']
    print(request.form)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, date, merchant)
    transaction_repository.save(transaction)
    return redirect("/transactions")

    