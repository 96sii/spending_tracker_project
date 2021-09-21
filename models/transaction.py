class Transaction:
    def __init__(self, amount, date, merchant, category, id=None):
        self.amount = amount
        self.date = date
        self.merchant = merchant
        self.category = category
        self.id = id


