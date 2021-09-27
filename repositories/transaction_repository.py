from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository



# select all function 
def select_all():
    transactions = []

    sql = "SELECT * FROM transactions ORDER BY date DESC"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        category = category_repository.select(row["category_id"])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    return transactions

# select all by merchant

def select_all_from_merchant(id):
    transactions = []

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = %s WHERE merchants.id = %s ORDER BY date DESC"
    values = [id, id]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(id)
        category = category_repository.select(row["category_id"])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    return transactions

def select_all_from_category(id):
    transactions = []

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = merchants.id INNER JOIN categories ON transactions.category_id = %s WHERE categories.id = %s ORDER BY date DESC"
    values = [id, id]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    return transactions


def select_all_from_date(date):
    transactions = []

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = merchants.id INNER JOIN categories ON transactions.category_id = categories.id WHERE date = %s"
    values = [date]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        category = category_repository.select(row["category_id"])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
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
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    for transaction in transactions:
        total += transaction.amount
        
    return total

def add_total_for_merchant(id):
    transactions = []
    total = 0

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = %s WHERE merchants.id = %s"
    values = [id, id]
    results = run_sql(sql, values)
 

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    for transaction in transactions:
        total += transaction.amount
        
    return total

def add_total_for_category(id):
    transactions = []
    total = 0

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = merchants.id INNER JOIN categories ON transactions.category_id = %s WHERE categories.id = %s"
    values = [id, id]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    for transaction in transactions:
        total += transaction.amount
        
    return total


def add_total_for_date(date):
    transactions = []
    total = 0

    sql = "SELECT * FROM transactions INNER JOIN merchants ON transactions.merchant_id = merchants.id INNER JOIN categories ON transactions.category_id = categories.id WHERE date = %s"
    values = [date]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, category, row['id'])
        transactions.append(transaction)

    for transaction in transactions:
        total += transaction.amount
        
    return total



#select by id
def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(result['amount'], result['date'], merchant, category, result['id'])
        return transaction


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(transaction):
    sql = "INSERT INTO transactions (amount, date, merchant_id, category_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.amount, transaction.date, transaction.merchant.id, transaction.category.id] 
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction



