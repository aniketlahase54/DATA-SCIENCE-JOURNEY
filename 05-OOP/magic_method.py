class fraction: 
    def __init__(self,num,den):
        self.num = num 
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other):
        new_num = self.num * other.den + self.den * other.num
        new_dev = self.den * other.den  

        return fraction(new_num,new_dev)  

    def __sub__(self,other):
        new_num = self.num * other.den - self.den * other.num
        new_dev = self.den * other.den  

        return fraction(new_num,new_dev)

    def __mul__(self,other):
        new_num = self.num * other.num
        new_dev = self.den * other.den

        return fraction(new_num,new_dev)

    def __truediv__(self,other):
        new_num = self.num * other.den
        new_dev = self.den * other.num

        return fraction(new_num,new_dev)


f1 = fraction(1,2)
print(f1)            

f2 = fraction(3,4)
print(f2)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)