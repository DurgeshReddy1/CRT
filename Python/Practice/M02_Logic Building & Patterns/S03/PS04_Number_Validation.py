''' 
Armstrong Number:
Input: 153
Output: Armstrong number

Input: 24
Output: Not an Armstrong number
'''
# num = int(input("Enter a number: "))
# count = len(str(num))
# s = 0
# for digit in str(num):
#     s+=int(digit) ** count    
# print("Armstrong Number" if s == num else "Not an Armstrong Number")

'''
Perfect Number
Input: 6
Output: Perfect Number
6 => 1,2,3
1+2+3 = 6
'''
# n = int(input("Enter a Number: "))
# s = 0
# for i in range(1,n//2+1):
#     if n % i == 0:
#         s += i
# print("Perfect Number" if s == n else "Not a Perfect Number")

'''
Strong Number:
Input: 123
Output: Not a Strong Number
Explanation: 1! + 2! + 3! = 1+2+6 = 9
'''
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "No factorial for -ve numbers"
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
num = int(input("Enter a number: "))
s = 0
for digit in str(num):
    s += factorial(int(digit))
print("Strong Number" if s == num else "Not a Strong Number")