'''
Debugging in Python
bug--> error
Finding and Fixing errors in program is called debugging.
Types of Errors:
1.Synatx Error --> missing colon, brackets, indentation error
2.Logical Error --> missing of logics
2.Runtime Error --> division by any number with number zero

Debugging Techniques:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a + b
print("The value of a is:", a) 
print("The value of b is:", b)
print("The sum of a and b is:", c)

Debugging Techniques:
    1.Print Statement Debugging  
    2.try-except
    3.use of pdb 
    4.use of IDE debugger
Purposes:
    1.pause the execution
    2.inspect variables values
    3.to run the code line by line
PDB Commands:
    1)n --> to get output in next line
    2)c --> to continue the execution
    3)p variable --> to print the value of a variable
    4)l --> list nearby code
    5)s --> start the function 
    6)r --> return from the function
    7)h --> to get help
    8)q --> to quit the execution 
try :
    a = int(input("Enter a: "))
    print(10/a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input.")
'''
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))      
print("The sum is:", add(num1,num2))