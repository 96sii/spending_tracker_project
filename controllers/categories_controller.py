from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.category import Category
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository

categories_blueprint = Blueprint("categories", __name__)

@categories_blueprint.route("/categories")
def categories():
    categories = category_repository.select_all()
    return render_template("/categories/index.html", categories=categories)

@categories_blueprint.route("/categories/new", methods=['GET'])
def new_category():
    return render_template("/categories/new.html")

@categories_blueprint.route("/categories", methods=['POST'])
def create_merchant():
    category_name = request.form['category_name']

    categories = category_repository.select_all()
    category_match = False
    for category in categories:
        if category_name == category.category:
            category_match = True
            
    if category_match == False:
        category = Category(category_name)
        category_repository.save(category)
        return redirect("/categories")
    else: 
        return redirect("/categories")


@categories_blueprint.route("/categories/<id>", methods=['GET'])
def show(id):
    category = category_repository.select(id)
    transactions = transaction_repository.select_all_from_category(id)
    total = transaction_repository.add_total_for_category(id)
    return render_template("/categories/show.html", category=category, transactions=transactions, total=total)