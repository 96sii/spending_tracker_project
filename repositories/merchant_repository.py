from db.run_sql import run_sql
from models.merchant import Merchant
import repositories.category_repository as category_repository

# select all function 
def select_all():
    merchants = []

    sql = "SELECT * FROM merchants ORDER BY name"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['logo'], row['id'])
        merchants.append(merchant)

    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['logo'], result['id'])
        return merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, logo) VALUES (%s, %s) RETURNING *"
    values = [merchant.name, merchant.logo]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def update(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = (merchant.name,  merchant.id)
    run_sql(sql, values)
    

