from db.run_sql import run_sql
from models.category import Category

def select_all():
    categories = []

    sql = "SELECT * FROM categories"
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