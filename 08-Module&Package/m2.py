import m1

print("Addition:",m1.add(5,3))
print("Subtraction:",m1.sub(5,3))

print("Class:",m1.car.car_type)
print("Model:",m1.car.model)

from m1 import add,sub

print(add(4,3))
print(sub(5,2))

import m1 as a 

print(a.add(4,3))
print(a.sub(5,2))

import math

print(math.sqrt(16))


import random 

print(random.randint(1,10))
