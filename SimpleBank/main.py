class BankAccount:
    def __init__(self,name,phnno,balance=0.00 ):
        self.name = name
        self.phnno = phnno
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"{self.name}'s account is deposited by {amount:2f}")
        else:
            print("Ïnvalid Amount")

    def withdraw(self,amount):
         if 0<amount<= self.balance:
             self.balance-=amount
             print(f"Succesfully withdrawled {amount} in {self.name}'s account")
         else:
             print("Invalid amount")               
    def getBalance(self):
        return f"Current balance in {self.name}'s account is {self.balance}"         
    
acc1 = BankAccount("Muke", "9845222602", 2000.0)
acc1.deposit(4000)
acc1.withdraw(2000)

print(acc1.getBalance())
