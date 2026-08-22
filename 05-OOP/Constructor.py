#parameter constructor

class student:
    clg_name = "SSBT COET JALGAON"

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def getdata(self):
        print(self.name,self.age)

    def show(self):
        print(self.clg_name)

s1 = student("Aniket",22)
s1.show()
s1.getdata()       


#defualt constructor 

class student:
    def __init__(self):
        self.clg_name = "SSBT COET JALGAON"

        print(self.clg_name)

s1 = student()        