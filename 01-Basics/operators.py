
# 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 2. Comparison Operators
x = 10
y = 20

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)


# 3. Logical Operators
age = 25

print("AND:", age > 18 and age < 60)
print("OR:", age < 18 or age > 60)
print("NOT:", not(age > 18))


# 4. Assignment Operators
number = 10

number += 5
print("+= :", number)

number -= 3
print("-= :", number)

number *= 2
print("*= :", number)

number /= 2
print("/= :", number)

number //= 2
print("//= :", number)

number %= 3
print("%= :", number)

number **= 2
print("**= :", number)


# 5. Membership Operators
languages = ["Python", "Java", "C++", "SQL"]

print("Python" in languages)
print("JavaScript" not in languages)


# 6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)


# 7. Bitwise Operators
p = 10
q = 4

print("Bitwise AND:", p & q)
print("Bitwise OR:", p | q)
print("Bitwise XOR:", p ^ q)
print("Bitwise NOT:", ~p)
print("Left Shift:", p << 1)
print("Right Shift:", p >> 1)