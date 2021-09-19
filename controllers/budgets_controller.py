from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
from models.budget import Budget
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import repositories.budget_repository as budget_repository




budgets_blueprint = Blueprint("budgets", __name__)


@budgets_blueprint.route("/budgets")
def budgets():
    budgets = budget_repository.select_all()
    total = transaction_repository.add_total()
    return render_template("budgets/index.html", budgets=budgets, total=total)

@budgets_blueprint.route("/budgets/<id>", methods=['GET'])
def show_budget(id):
    budget = budget_repository.select(id)
    return render_template("budgets/show.html", budget=budget)


@budgets_blueprint.route("/budgets/<id>/edit", methods=['GET'])
def edit_budget(id):
    budget = budget_repository.select(id)
    return render_template("/budgets/edit.html", budget=budget)


@budgets_blueprint.route("/budgets/<id>", methods=['POST'])
def update_budget(id):
    budget_amount = request.form['budget']
    budget_1 = Budget(budget_amount, id)
    budget_repository.update(budget_1)
    return redirect('/budgets')


