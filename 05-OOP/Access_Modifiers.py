# public access modifiers:-
# default modifire
# inside class
# outside class
# differant class

class student: 
    def __init__(self):
        self.name = "Aniket"  #public variable

    def show(self):
        print(self.name)


s1 = student()
print(s1.name)
s1.show()            

# protected access modifier:-
# -variable name
# inside class
# another class

class student: 
    def __init__(self):
        self._name = "Aniket"  #public variable

    def show(self):
        print(self._name)

class child(student): 
    def display(self):
        print(self._name)



s1 = student()
print(s1._name)
s1.show()  

c=child()
print(c._name)
c.display()

# private access modifier:-
# __variable name
# within class access 
# inside the class
# outside are not allowed

class student: 
    def __init__(self):
        self.__name = "Aniket"  #private variable

    def show(self):
        print(self.__name)

# class child(student): 
#     def display(self):
#         print(self.__name)

# c=child()
# print(c.__name) #error
# c.display()

s1 = student()
# print(s1.__name)  #error
s1.show()  #run

print(s1._student__name) #data,name mangling



class bank:
    def __init__(self): 
        self.name = "Aniket"    #public
        self._balc = 50000    #protected
        self.__pin = 12345   #private

    def show(self):
        print(self.name,self._balc,self.__pin)


b1 = bank()
print(b1.name)    #public 
b1._balc = 75000   
print(b1._balc)     # not recommanded

# print(b1.__pin)  # got error
print(b1._bank__pin)
b1.show()