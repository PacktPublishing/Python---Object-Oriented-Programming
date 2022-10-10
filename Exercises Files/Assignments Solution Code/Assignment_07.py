class BankAccount():
    def __init__(self,number,holder,balance):
        self.number = number
        self.holder = holder
        self.balance = balance
        
    def __str__(self):
        return f"BankAccount({self.number},{self.holder},{self.balance})"
    
    def __add__(self,other):
        if isinstance(other,(int,float)):
            return BankAccount(self.number,self.holder,self.balance+other)
        
        elif isinstance(other,Check):
            if other.number == self.number:
                return BankAccount(self.number,self.holder,self.balance+other.amount)
            else:
                raise ValueError("Mismatched account number and check number")
        
        else:
            raise ValueError(f"+ is not defined between BankAccount and {other.__class__.__name__}")
        
    def __radd__(self,other):
        return self+other
    
    def __sub__(self,other):
        if isinstance(other,(int,float)):
            if self.balance<other:
                raise ValueError("Amount exceeds the balance limit")
            else:
                return BankAccount(self.number,self.holder,self.balance-other)
        
        else:
            raise ValueError(f"+ is not defined between BankAccount and {other.__class__.__name__}")
        
    def __rsub__(self,other):
        return self-other
        
class Check():
    def __init__(self,number,amount):
        self.amount = amount
        self.number = number

if __name__ == "__main__":  
    account1 = BankAccount(123,"Alex",50)
    print(account1)
    account1 = account1+20
    print(account1)
    account1 = account1 -20
    print(account1)
    # account1 = account1 - 100
    # print(account1)

    ch1 = Check(123, 100)
    ch2 = Check(999,200)

    account1 = account1+ch1
    print(account1)
    account1 = account1+ch2
    print(account1)
