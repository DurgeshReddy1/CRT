'''
1) Find the largest number in a list using the built-in function max().
2) Check pallindrone string using built-in function reversed() and join()
3) Count Even numbers using filter()
4)Remove duplicates from a list using set()
5)Sum of digits in a number using sum() 
6)Sort words Alphabetically using sorted()
7)Find Common Elements in two lists using set() 
8)Index with value using enumerate()
9)Pair two lists using zip()
10)Find second largest number in a list using sorted() 
'''
#1) Find the largest number in a list using the built-in function max().
a=[10,20,87,15,98,12,3,2,45,100] 
print(max(a))

#2) Check palindrome string using built-in function reversed() and join()
s=input("Enter a string: ")
if s == ''.join(reversed(s)):
    print("The string is a palindrome.")
else:    
    print("The string is not a palindrome.") 

#3) Count Even numbers using filter()
a=[10,20,87,15,98,12,3,2,45,100]
res = list(filter(lambda x: x%2==0, a))
print(res)
print(len(res))

#4)Remove duplicates from a list using set()
a=[10,20,87,15,98,12,3,2,45,100,1,2,10]
print(set(a))

#5)Sum of digits in a number using sum() 
n=12345
res = sum(int(digit) for digit in str(n))
print(res)

#6)Sort words Alphabetically using sorted()
words = ["banana", "apple", "cherry", "date"]
print(sorted(words))   

#7)Find Common Elements in two lists using set() 
a=[1,2,3,45,5]
b=[2,4,5,45,5,10]
print(set(a) & set(b))
print(res)
print(tuple(res))

#8)Index with value using enumerate()
words = ["banana", "apple", "cherry", "date"]
for index, val in enumerate(words):
    print(index, val)

#9)Pair two lists using zip()
a=[1,23,45,6,7]
b=[2,8,5,9,4,5]
print(zip(a,b))

#10)Find second largest number in a list using sorted() 
b=[2,8,5,9,4,5]
b.sort()
print(b[-2])

