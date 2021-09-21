from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import repositories.transaction_repository as transaction_repository



merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("/merchants/index.html", merchants=merchants)



@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_merchant():
    return render_template("merchants/new.html")



@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    merchant_name = request.form['merchant_name']

    merchants = merchant_repository.select_all()
    merchant_match = False
    for merchant in merchants:
        if merchant_name == merchant.name:
            merchant_match = True
            
    if merchant_match == False:
        merchant = Merchant(merchant_name)
        merchant_repository.save(merchant)
        return redirect("/merchants")
    else: 
        return redirect("/merchants")



@merchants_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    transactions = transaction_repository.select_all_from_merchant(id)
    total= transaction_repository.add_total_for_merchant(id)
    return render_template("merchants/show.html", merchant=merchant, transactions=transactions, total=total)


@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("/merchants/edit.html", merchant=merchant)


@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    merchant_name = request.form['merchant_name']
    merchant = Merchant(merchant_name, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')