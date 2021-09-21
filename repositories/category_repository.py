from db.run_sql import run_sql
from models.category import Category
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository

def select_all():
    categories = []

    sql = "SELECT * FROM categories ORDER BY category"
    results = run_sql(sql)

    for row in results:
        category = Category(row['category'], row['id'])
        categories.append(category)
    
    return categories



def select(id):
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        category = Category(result['category'], result['id'])
        return category

def save(category):
    sql = "INSERT INTO categories (category) VALUES (%s) RETURNING *"
    values = [category.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

def update(category):
    sql = "UPDATE categories SET category = %s WHERE id = %s"
    values = (category.category, category.id)
    run_sql(sql, values)