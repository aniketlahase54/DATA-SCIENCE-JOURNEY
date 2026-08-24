from abc import ABC,abstractmethod


#Abstract class 
class Bank(ABC):

    @abstractmethod
    def deposite(self,amount):
        pass 

    @abstractmethod
    def withdraw(self,amount):
        pass 

    @abstractmethod
    def check_balc(self):
        pass


class SBI(Bank): 
    def __init__(self,balc):
        self.balc = balc


    def deposite(self,amount):
        self.balc+=amount
        print("Deposited:",amount)   

    def withdraw(self,amount):
        if amount <= self.balc:
            self.balc-=amount
            print("Withdraw:",amount)
        else: 
            print("Insufficeient Balance")

    def check_balc(self):
        print("Your Current Balance:",self.balc)


acc1 = SBI(20000)        
acc1.deposite(5000)
acc1.withdraw(10000)
acc1.check_balc()