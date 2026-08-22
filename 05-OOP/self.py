class student:
    name = "Aniket"
    age = 23

    def show(self):
        print(self.name,self.age)
      

s1 = student()
s1.show()    #student.show(s1)

class student:
    def show(self):
        print("Hello")


s1=student()
s1.show()

class student:
    def setData(self,name,age):
        self.name = name
        self.age = age


    def getData(self):
        print(self.name,self.age)     



s1 = student()        
s1.setData("Aniket",22)
s1.getData()

s2 = student()        
s2.setData("Om",2)
s2.getData()