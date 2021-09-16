import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository

print(category_repository.select_all())
print(merchant_repository.select_all())