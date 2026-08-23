#how attribute access

class student :
    def __init__(self,name): 
        self.name = name

s1 = student("Aniket")
print(s1.name)

class test:
    x = 10 

t = test()
print(t.x)    

class A: 
    def show(self): 
        print("hello")

obj = A()
obj.show()        


#Attribute creation outside the class

class student: 
    pass

s1 = student()
s1.age = 23
print(s1.age)

s2 = student()
print(s2.age)


#Reference Variable
a = [1,2,3]
print(id(a))

b = a
print(id(b))
print(a is b)


#object delete

a = [10,5]

b = a
c = a
del a
print(b)
print(c)


#pass by reference  (obj reference)
def change(lst): 
    lst.append(100)

a = [1,50]
change(a)
print(a)    


#call by value (immutable case)
def change(x):
    x = x+10

a = 6
change(a)
print(a)    