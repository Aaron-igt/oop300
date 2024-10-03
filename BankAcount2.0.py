class BankAccount:

# creating a class variable
    interest_rate = 0.05

# creatig the constructor to hold all the instance variables of the objects.
    def __init__(self ,account_holder ):
        self.account_holder = account_holder
        self.balance = 0
    
# creating a method deposit inorder to show that the account_holder deposited a certain amount onto his or her account
# we show this action by adding the amount being added to the account with the current balance, we add the argument of amount in
# the method definition inorder to pass the amount to be added to the method.
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited shs.{amount}, the new balance is shs.{self.balance}.")
    
# Creating a method withdraw and do perform a condition to tell the customer if their accounts have the amount of money they want
# to withdraw, we pass the argument amount1 representing the amount the account holder is withdrawing from their account.
    def withdraw(self, amount1):
        if amount1 <= self.balance:
            self.balance -= amount1
            print(f"{self.account_holder} has withdrawn shs.{amount1} from his account.")
        else:
            print("Insufficient funds.")
            
# creating a method to apply the interest rate that we defined in the class variable interest_rate, this is added to the current 
# balance an account holder has on their account.
    def apply_interest(self):
        interest_amount = self.balance * BankAccount.interest_rate
        self.balance += interest_amount
        print(f"An interest of {interest_amount} has been added to shs.{self.balance}.")
        
# created a method display_account_info, this is used to display the name of the account holder and their initial balance
# on their account
    def display_account_info(self):
        print(f"Account holder name: {self.account_holder}.")
        print(f"Current balance: shs.{self.balance}.")
    
# creating the objects that are required for the program to run, in this case it's the accounts and their holder's names
Account1 = BankAccount("Aaron")
Account2 = BankAccount("Joshua")

# Performing deposits and withdraws 
Account1.deposit(500)
Account1.withdraw(200)
Account2.deposit(1000)
Account1.withdraw(300)

# applying interest 
Account1.apply_interest()
Account2.apply_interest()

# displaying account information
Account1.display_account_info()
Account2.display_account_info()