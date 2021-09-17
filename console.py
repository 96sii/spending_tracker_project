import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import repositories.transaction_repository as transaction_repository
from models.transaction import Transaction
from models.merchant import Merchant
from models.category import Category

clothing = Category('Clothing')
merchant = Merchant('Depop', clothing)
transaction = Transaction(4.5, '2021-09-14', merchant)

category_repository.save(clothing)
merchant_repository.save(merchant)

transaction_repository.save(transaction)

