from db.run_sql import run_sql
from models.budget import Budget
import repositories.transaction_repository as transaction_repository

def select_all():
    categories = []

    sql = "SELECT * FROM budgets"
    results = run_sql(sql)

    for row in results:
        budget = Budget(row['amount'], row['id'])
        categories.append(budget)
    
    return categories

def select(id):
    budget = None

    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = Budget(result['amount'], result['id'])
        return budget

def save(budget):
    sql = "INSERT INTO budgets (amount) VALUES (%s) RETURNING *"
    values = [budget.amount]
    results = run_sql(sql, values)
    id = results[0]['id']
    budget.id = id
    return budget


def update(budget):
    sql = "UPDATE budgets SET amount = %s WHERE id = %s"
    values = (budget.amount, budget.id)
    run_sql(sql, values)

def budget_percentage(budget):
    total = transaction_repository.add_total()
    budget_left = budget.amount - total
    budget_percentage = ((budget_left/budget.amount)*100)
    return budget_percentage