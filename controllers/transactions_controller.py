from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import repositories.budget_repository as budget_repository




transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.add_total()
    budget = budget_repository.select(1)
    return render_template("/transactions/index.html", transactions=transactions, total=total, budget=budget)


@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    categories = category_repository.select_all()
    merchants = merchant_repository.select_all()
    
    return render_template("transactions/new.html", categories=categories, merchants=merchants)


@transactions_blueprint.route("/transactions", methods=['POST'])
def add_transaction():
    merchant_name = request.form['merchant_name']
    category_id = request.form['category_id']
    amount = request.form['amount']
    date = request.form['date']
    category = category_repository.select(category_id)

    merchants = merchant_repository.select_all()
    for merchant in merchants:
        if merchant.name == merchant_name:
            merchant_1 = merchant
            transaction = Transaction(amount, date, merchant_1)
            transaction_repository.save(transaction)
            return redirect("/transactions")
        else:
            merchant_1 = Merchant(merchant_name, category)
            merchant_repository.save(merchant_1)
            transaction = Transaction(amount, date, merchant_1)
            transaction_repository.save(transaction)
            return redirect("/transactions")
        

@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete(id):
    transaction_repository.delete(id)   
    return redirect("/transactions")