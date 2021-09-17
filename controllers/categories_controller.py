from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository

categories_blueprint = Blueprint("categories", __name__)

@categories_blueprint.route("/categories")
def categories():
    categories = category_repository.select_all()
    return render_template("/categories/index.html", categories=categories)

