class Transaction:
    def __init__(self, amount, date, merchant, id=None):
        self.amount = amount
        self.date = date
        self.merchant = merchant
        self.id = id