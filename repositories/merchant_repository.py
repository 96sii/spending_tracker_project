from db.run_sql import run_sql
from models.merchant import Merchant
import repositories.category_repository as category_repository

# select all function 
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)

    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
        return merchant

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant




            

