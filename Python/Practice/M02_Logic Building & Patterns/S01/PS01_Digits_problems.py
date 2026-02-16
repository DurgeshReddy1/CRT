'''
sample input : 123445
sample output : 4

sample input : 455786
sample output : 6

sample input : 45
sample output : 2
'''
# digits = int(input("Enter the number: "))
# count = 0 
# while digits > 0:
#     count += 1
#     digits //= 10
# print("Number of digits: ", count)

# print(len(str(digits))) # Alternative method

'''
sample input : 1565
sample output : 17

sample input : 1234
sample output : 10  
'''
# digits = int(input("Enter the number: "))
# temp = digits
# sum_of_digits = 0   
# while digits > 0:
#     sum_of_digits += digits % 10
#     digits //= 10   

# print("Sum of digits: ", sum_of_digits)
# print("Sum of digits using alternative method: ", sum(map(int, str(temp))))

'''
sample input : 12345
sample output : 2 3

sample input : 5588
sample output : 2 2
'''
# n = int(input("Enter the number: "))
# count_even = 0
# count_odd = 0       
# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
#     n //= 10
# print(count_even, count_odd)

'''
sample input : 546
sample output : 6 

sample input : 786
sample output : 9
'''
# n = int(input("Enter the number: "))
# s = 0
# while n > 9:
#     n = sum(map(int, str(n)))
# print(n)

n = int(input("Enter the number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10    
print("Reversed number: ", rev) 