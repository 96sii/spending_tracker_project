from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository


# select all function 
def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        transaction = Transaction(row['amount'], row['date'], merchant, row['id'])
        transactions.append(transaction)

    return transactions

# select all by merchant
def select_all_from_merchant(id):
    transactions = []

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = %s WHERE merchants.id = %s"
    values = [id, id]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(id)
        transaction = Transaction(row['amount'], row['date'], merchant, row['id'])
        transactions.append(transaction)

    return transactions

# add total transactions
def add_total():
    transactions = []
    total = 0

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        transaction = Transaction(row['amount'], row['date'], merchant, row['id'])
        transactions.append(transaction)

    for transaction in transactions:
        total += transaction.amount
        round_total = "{:.2f}".format(total)
    return round_total

def budget(total, budget):
    if budget > total: 
        return f"You have {budget - total} left to spend"
    else: 
        return f"You have gone over your budget by {total - budget}"

#select by id
def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(result['amount'], result['date'], merchant, result['id'])
        return transaction


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(transaction):
    sql = "INSERT INTO transactions (amount, date, merchant_id) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction.amount, transaction.date, transaction.merchant.id] 
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction



