class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def paid(self):
        print(f"Paid: {self.amount}")

class Cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    
class Momo(Payment):
    def __init__(self, amount, merchantCode):
        super().__init__(amount)
        self.merchantCode = merchantCode

class Visa(Payment):
    def __init__(self, amount, cvc):
        super().__init__(amount)
        self.cvc = cvc
        
class Onamanja(Payment):
    def __init__(self, amount, contact, nationalID, address, nextKin, witness):
        super().__init__(amount)
        self.contact = contact
        self.nationalID = nationalID
        self.address = address
        self.nextKin = nextKin
        self.witness = witness
    