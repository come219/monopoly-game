class Bank:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def __str__(self):
        return f"Bank (${self.balance})"

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance -= amount
