class Bank:
    def __init__(self,name,balc):
        self.name = name   #public variable
        self.__balc = balc   #private variable

    #getter method
    def get_balc(self): 
        return self.__balc

    #setter method
    def set_balc(self,new_balc): 
        self.__balc = new_balc

acc1 = Bank("Aniket",40000)
print(acc1.name)
print(acc1.get_balc())

acc1.set_balc(50000)
print(acc1.get_balc())
