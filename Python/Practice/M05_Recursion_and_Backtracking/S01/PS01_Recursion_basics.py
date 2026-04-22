#Sum of n natural numbers
n = int(input("Enter a number: "))
def natural_numbers(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print(natural_numbers(5))
print(natural_numbers(10))

#Recursion Approach 
def natural_numbers(n):
    if n == 1:
       return 1     
    return n + natural_numbers(n-1)
print(natural_numbers(5))
print(natural_numbers(10))

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(4))

#Fibonacci Series n th term
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(10))