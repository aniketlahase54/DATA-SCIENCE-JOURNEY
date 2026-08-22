class student:
    clg_name = "GCOET JALGAON"

    @classmethod
    def change_clg_name(cls,new_name):
        cls.clg_name = new_name

    @staticmethod
    def add(a,b):
        return a+b    


student.change_clg_name("SSBT COET JALGAON")
print(student.clg_name)

print(student.add(5,3))

#mini project
# Product Store
# Design & create an online store for products (name, prices)
# Track total product created
# Create a static method to calculate discount on each product based on % parameter.

class store:
    count = 0    #class variable

    def __init__(self,name,price):
        self.name = name    #instance varible
        self.price = price
        store.count+=1

    def get_info(self):    #instance method
        print(self.name,self.price)

    @classmethod
    def get_count(cls):
        print(f"Total product: {cls.count}")

    @staticmethod
    def discount(price,per):
        dis = price -((price*per)/100)
        print(f"discounted price : {dis}")

         

p1 = store("Pen", 10)
p1.get_info()
p2 = store("notebook",50)
p2.get_info()

store.get_count()
store.discount(5000,20)