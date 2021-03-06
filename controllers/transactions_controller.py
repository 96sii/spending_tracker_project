from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import datetime
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
    budget_percentage = budget_repository.budget_percentage(budget)
    if budget_percentage < 0:
        budget_percentage = 0
    return render_template("/transactions/index.html", transactions=transactions, total=total, budget=budget, budget_percentage=budget_percentage)


@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    categories = category_repository.select_all()
    merchants = merchant_repository.select_all()
    
    return render_template("transactions/new.html", categories=categories, merchants=merchants)


@transactions_blueprint.route("/transactions", methods=['POST'])
def add_transaction():
    merchant_name = request.form['merchant_name']
    logo = request.form['logo']
    category_id = request.form['category_id']
    amount = request.form['amount']
    date = request.form['date']
    category = category_repository.select(category_id)

    merchants = merchant_repository.select_all()
    merchant_match = False

    for merchant in merchants:
        if merchant_name == merchant.name:
            print (merchant.name)
            merchant_match = True

        if merchant_match == True: 
            merchant_1 = merchant
            transaction = Transaction(amount, date, merchant_1, category)
            transaction_repository.save(transaction)
            return redirect ('/transactions')



    if merchant_match == False:
        print ("Merchant not found")
        merchant_2 = Merchant(merchant_name, logo)
        merchant_repository.save(merchant_2)
        transaction = Transaction(amount, date, merchant_2, category)
        transaction_repository.save(transaction)
        return redirect ('/transactions')



@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete(id):
    transaction_repository.delete(id)   
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<date>", methods=['GET'])
def show_date(date):
    date_1 = date
    total = transaction_repository.add_total_for_date(date)
    transactions = transaction_repository.select_all_from_date(date)
    return render_template("/transactions/date.html", total=total, transactions=transactions, date_1=date_1)