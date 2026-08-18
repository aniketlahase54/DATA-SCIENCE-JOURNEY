num = int(input("enter the number"))

for i in range(1,11):

    print(i*num)


num = int(input("enter the number:"))
sum = 0
for i in range(1,num+1):
    sum = sum+i

print(sum)    


name = "Python"
for i in name:
    print(i)

marks = [22,43,65,78,23,54,77,56,97]
total = 0
for i in marks:
    print(i)  


marks = [22,43,65,78,23,54,77,56,97]
total = 0
for i in marks:
    total = total+i
print(total)    


t = (2,34,44,5,3,4,22,23,42)
for i in t:
    print(i)

marks = [22,43,65,78,23,54,77,56,97]
total = 0
for i in marks:
    print(i)    

s = {22,33,44,55,66,7,64,36}
sum = 0
for i in s:
    sum = sum+i
print(sum)

student = {
    "name" : "Aniket",
    "Age" : 22
}


for key in student:
    print(key,student[key])

for k,v in student.items():
    print(k,"=",v)

for i in range (1,5):
    for jf in range(1,5):
        print("*", end = " ")
    print()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for element in row:
        print(element , end= " ")
    print()    

n = 5
for i in range (n):
    for jf in range(n):
        print(chr(65+i), end = " ")  #65=askci value
    print()



for i in range (1,5):
    for j in range(1,5):
        print(j,end = " ")
    print()

for i in range (1,6):
    for j in range(1,6):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
   
    print() 

# *         
# * *       
# * * *     
# * * * *   
# * * * * *    


for i in range (1,6):
    for j in range(1,6):
        if j<=6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
   
    print() 
# * * * * * 
# * * * *   
# * * *     
# * *       
# * 


for i in range (1,6):
    for j in range(1,6):
        if j>=6-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
   
    print() 

#          * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

for i in range (1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
   
    print()
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

for i in range (1,6):
    for j in range(1,6):
        if j<=i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
   
    print() 

# 1         
# 1 2       
# 1 2 3     
# 1 2 3 4   
# 1 2 3 4 5     

for i in range (1,5):
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
   
    print() 

#       *       
#     * * *     
#   * * * * *   
# * * * * * * *     


num = int(input("enter the no:"))
flag = 0

if num<2:
    print("not prime")
    flag = 1

else:
    for i in range(2, num):
        if num%i==0:
            print("not prime")
            flag = 1
            break
if flag == 0:
    print("prime")               



s = int(input("enter the start no:"))
e = int(input("enter the end no:"))
count = 0
for i in range(s,e+1):
    if i < 2:
        continue
    flag=0


    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag== 0:
        count+=1
        print(i)    
print("Count of prime number in given range",count)