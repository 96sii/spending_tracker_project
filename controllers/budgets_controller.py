from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository




budgets_blueprint = Blueprint("budgets", __name__)


@budgets_blueprint.route("/budgets")
def budgets():
    return render_template("budgets/index.html")

@budgets_blueprint.route("/budget/new", methods=['GET'])
def budget():
    return render_template("transactions/budget.html")

@budgets_blueprint.route("/budget", methods=['POST'])
def create_budget():
    budget = request.form['budget']