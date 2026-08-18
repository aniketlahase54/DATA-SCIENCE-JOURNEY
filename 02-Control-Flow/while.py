
n = int(input("Enter the number: "))
i = 0
while i <= n:
    if i == 15:
        i += 1
        continue
    print(i)
    i += 1


num = int(input("enter the number:"))
i = 1
while i<=10:
    print(num*i)
    i+=1


num = int(input("enter the no:"))
i = 1
while i<=num:
    print(i)
    i+=1

num = int(input("enter the no:"))
i = 1
while i<=num:
    if i%2==0:
        print(i)

    i+=1    

start = int(input("enter the start no:"))
end = int(input("enter the end no"))

i = start

while i<=end:
    if i % 2 != 0:
        print(i)

    i+=1    

n = int(input("Enter N: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)


num = int(input("enter the no:"))

count = 0

while num>0:
    num//=10
    count+=1

print(count)   



num = int(input("enter the no:"))
rev = 0 
while num>0:
    digit = num%10
    rev = rev * 10 + digit
    num//=10

print(rev)    
