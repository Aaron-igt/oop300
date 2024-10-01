class BankAccount:
    
    total_accounts = 0
    
    def __init__(self ,account_holder_name ,initial_balance):
        self.account_holder_name = account_holder_name
        self.initial_balance = initial_balance
        BankAccount.total_accounts += 1
        
    def deposit(self, amount):
        new_amount = self.initial_balance + amount
        print(f"{self.account_holder_name} has deposited {amount}, New balance is {new_amount}.")
        
    def withdraw(self, amount1):
        if amount1 > self.initial_balance:
            print("insufficient funds.")
        else:
            self.initial_balance -= amount1
            print(f"{self.account_holder_name} has withdrawn {amount1}.")
        
    def display(self):
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Current Balance: {self.initial_balance}")
     
    @classmethod    
    def get_total_accounts(cls):
        return cls.total_accounts
        
Account1 = BankAccount("Aaron Nsajuli", 20000)
Account2 = BankAccount("Ricky Myles", 15000)
Account3 = BankAccount("Marcus Rashford", 20000)

Account1.deposit(3000)
Account2.withdraw(30000)
Account1.display()
print(BankAccount.get_total_accounts())