#functional Polymorphism (built in polymorphism)

print(len("Aniket"))
print(len([1,2,3,4,5]))
print(len((1,2,3,4,5,6,7,8)))


#Operator Overloading (Operator Polymorphism )

print("Aniket" + "Lahase")
print(5+3)
print([1,2,3]+[4,5,6])
print((1,2,3)+(4,5,6))

#Custom Operator Overloading


class student:
    def __init__(self,marks):
        self.marks = marks

    def __add__(self,other):
        return self.marks + other.marks

s1 = student(40)
s2 = student(56)        
print(s1 + s2)


#Method Overriding (Runtime Polymorphism )

class animal:
    def sound(self): 
        print("Animal Make a Sound")


class Dog(animal): 
    def sound(self): 
        super().sound()
        print("Dog barks")

class Cat(animal): 
    def sound(self):
        super().sound()
        print("Cat Meows")

a = animal()
a.sound()
d = Dog()
d.sound()
c = Cat()
c.sound()

#Duck Typing Polymorphism

class Laptop: 
    def code(self): 
        print("Coding On Laptop")


class Mobile: 
    def code(self): 
        print("Codind on Mobile")        



def prefrom_coding(device):
    device.code()        

l = Laptop()
m = Mobile()

prefrom_coding(l)
prefrom_coding(m)