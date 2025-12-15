class BankAccount():
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
    
    def check_balance(self):
        print("Your current balance is now : ",self.balance)
    
    def deposit(self,amt):
        if(amt<0):
            print("Amount can't be negative")
            return
        else:
            self.balance=self.balance+amt
    
    def withdraw(self,amt):
        if(self.balance<amt):
            print("Insufficient Balance")
            return
        self.balance=self.balance-amt
    
    def transfer(self,account,amt):
        if(self.balance<amt):
            print("Insufficient Balance")
            return
        elif(amt<0):
            print("Amount can't be negative")
            return
        else:
            account.balance+=amt
            self.balance-=amt


acc1=BankAccount(123,"Arjun",500)
acc2=BankAccount(124,"Karan",500)

#Bank Application using OOPs python concept completed



acc1.deposit(500)

# acc1.check_balance()

acc1.transfer(acc2,500)
acc1.check_balance()
acc2.check_balance()

