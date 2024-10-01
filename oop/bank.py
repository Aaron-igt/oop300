class bankAccount:
    interest_rate = 0.05
    
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def add_interest(self):
        self.balance += self.balance * bankAccount.interest
        return self.balance
    
ThomasAccount.deposit = bankAccount(50000)

