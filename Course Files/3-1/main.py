class BankAccount:
    interest_rate = 1.5
    population = 0
    
    def __init__(self,number,holder,balance):
        self.number = number
        self.holder = holder
        self.balance = balance
        BankAccount.population+=1
        
    def calculate_interest(self):
        interest = self.balance * BankAccount.interest_rate
        return interest
        
acc1 = BankAccount(123,"Alex",20)
print(BankAccount.interest_rate)
print(acc1.interest_rate)

acc2 = BankAccount(123,"Bob", 10)
print(acc2.interest_rate)
BankAccount.interest_rate = 2.5
print(BankAccount.interest_rate , acc1.interest_rate , acc2.interest_rate)

print(acc1.calculate_interest())
print(acc2.calculate_interest())

print(BankAccount.population)
