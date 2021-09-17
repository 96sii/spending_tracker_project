from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository



merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("/merchants/index.html", merchants=merchants)

@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_merchant():
    categories = category_repository.select_all()
    return render_template("merchants/new.html", categories=categories)

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    merchant_name = request.form['merchant_name']
    category_id = request.form['category_id']
    category = category_repository.select(category_id)
    merchant = Merchant(merchant_name, category)
    merchant_repository.save(merchant)
    return redirect("/merchants")