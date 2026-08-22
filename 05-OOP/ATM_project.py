class ATM:
    def __init__(self,balc,pin):
        self.balc = balc
        self.pin = pin
    
    def check_pin(self):

        user_pin = int(input("enter the pin:"))

        if user_pin == self.pin:
            print("Valid Pin")
            return True

        else:
            print("Invalid Pin") 
            return False    

    def check_balc(self):
        if self.check_pin(): 
            print(f"Balance: {self.balc}")

    def deposit(self,amount):
        if self.check_pin():
            self.balc += amount
            print("deposit successful")

    
    def withdraw(self,amount):
        if self.check_pin():
            if amount>self.balc:
                print("insfficient balance")
            else:
                self.balc-=amount
                print("withdraw successful")

        

    def change_pin(self):
        newpin=int(input("enter the new pin"))
        self.pin = newpin
        pass 

    def menu (self):
        while True:
            print("\n1:check pin")
            print("\n2:check balance")
            print("\n3:deposit")
            print("\n4:withdaw")
            print("\n5:change pin")
            print("\n6:exit")

            choice = int(input("enter the choice:"))

            if choice==1:
                self.check_pin()

            elif choice==2:
                self.check_balc()

            elif choice == 3:
                amt = int(input("enter the amount:"))
                self.deposit(amt)

            elif choice == 4:
                amt = int(input("enter the amount:"))
                self.withdraw(amt)

            elif choice == 5:
                self.change_pin()

            else:
                exit()    
                   

t1 = ATM(20000,12345)
t1.menu()