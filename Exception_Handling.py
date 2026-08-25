try: 
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    result = num1 / num2
    print("The result is: ",result)

except: 
    print("An error occurred. Please check your input and try again")    

#Specific Exception Handling

try: 
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    result = num1 / num2
    print("The result is: ",result)

except ZeroDivisionError: 
    print("You Cannot Divide by Zero. please enter a non-zero number")    

except ValueError:
    print("Invalid input. Please enter a valid number") 

#else block in Exception Handling

try: 
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    result = num1 / num2
    

except ZeroDivisionError: 
    print("You Cannot Divide by Zero. please enter a non-zero number")    

except ValueError:
    print("Invalid input. Please enter a valid number") 
else:
    print("The result is: ",result)

#Finally block in Exception Handling

try: 
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    result = num1 / num2
    

except ZeroDivisionError: 
    print("You Cannot Divide by Zero. please enter a non-zero number")    

except ValueError:
    print("Invalid input. Please enter a valid number") 
else:
    print("The result is: ",result)

finally: 
    print("Thank you for using the calculator ")    


#raiseing exception (custom exception)

age =int(input("enter the age: "))
if age < 18 :
    raise ValueError("You must be at least 18 years old to access this content")
else: 
    print("Welcome! you have access to this content...")    

#Multiple exception in single except block

try: 
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    result = num1 / num2
    print("The result is: ",result)


except (ZeroDivisionError,ValueError):
    print("Either you entered a non numeric value or tried to divide by zero input and try again....")


#Exception as e

try: 
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    result = num1 / num2
    print("The result is: ",result)


except (ZeroDivisionError,ValueError) as e:
    print("An error occurred: ",e)   



#real word example as exception handling


try: 
    balc = 1000
    amount = int(input("enter the amount to withdraw: "))

    if amount > balc: 
        raise ValueError("insufficient fund.. your current balance is: $"+str(balc))

    else: 
        balc-=amount
        print("Withdraw Successful... your new balance is: $"+str(balc))
except Exception as e:
    print("An error occurred:",e)

finally: 
    print("Thank You for using banking services")                