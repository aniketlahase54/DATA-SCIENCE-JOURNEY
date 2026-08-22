#class variable

class student:
    clg_name = "SSBT COET JALGAON" # Class variable


s1 = student()
student.clg_name = "DY Patil Pune"
print(s1.clg_name)

s2 = student()
print(s2.clg_name)

s3= student()
print(s3.clg_name)


#instance variable

class student:
    clg = "SSBT COET JALGAON"

    def __init__(self,name):       #instance variable
        self.name = name
         

s1 = student("Aniket")
print(s1.name)

s2 = student("Om")
print(s2.name)


#instance method

class student:
    clg = "SSBT COET JALGAON"

    def __init__(self,name):       #instance variable
        self.name = name
         
    def show(self):        #instance method

        print(self.name)

s1 = student("Aniket")
s1.show()

s2 = student("Om")
s2.show()