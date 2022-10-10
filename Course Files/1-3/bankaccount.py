class BankAccount:
    def __init__(self,holder , number ,balance =0):
        print("A new bank account was created")
        self.number  = number
        self.holder = holder
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            
        else:
            print("Not Enough Money")

    def __str__(self):
        return f"Bank Account {self.number},{self.holder},{self.balance}"
    