#Single-level Inheritance

class father: 
    def house(self): 
        print("father has a house")


class son(father): 
    def car (self): 
        print("son has a car")


s = son()
s.car()
s.house()        

#Multi-level Inheritance

class grandfather: 
    def land(self): 
        print("grandfather has a land")

class father(grandfather): 
    def house(self): 
        print("father has a house")

class son(father): 
    def car (self): 
        print("son has a car")

s = son()
s.car()
s.house()        
s.land()


#multiple Inheritance

class father: 
    def fshow(self): 
        print("father has a house")


class mother: 
    def mshow(self): 
        print("mother has a car")


class son(father,mother): 
    def sshow(self): 
        print("child has a bike")        

s = son()
s.fshow()
s.mshow()
s.sshow()


#Hierarchical Inheritance

class father: 
     def fshow(self): 
        print("father has a house")


class Aniket(father):
    def Aniket_show(self): 
        print("Aniket has a car")

class Amit(father):
    def Amit_show(self): 
        print("Amit has a bike")

a = Aniket()
a.fshow()
a.Aniket_show()    

A = Amit()
A.Amit_show()
A.fshow()


#super method


class A : 
    def __init__(self): 
        print("A Constructor")

class B(A): 
    def __init__(self):
        super().__init__()
        print("B Constructor")        

b = B()
        


#Method overriding

class A : 
    def sound(self): 
        print("A Constructor")

class B(A): 
    def sound(self):
        super().sound()
        print("B Constructor")        

b = B() 
b.sound()       
# b.sound()       



class preson:
    def __init__(self,name): 
        self.name = name 


    def display(self): 
        print("Name:",self.name)    


class student(preson):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
    
        super().display()
        print("Roll No:",self.roll_no)


s1 = student("Aniket",101)
s1.display()                   