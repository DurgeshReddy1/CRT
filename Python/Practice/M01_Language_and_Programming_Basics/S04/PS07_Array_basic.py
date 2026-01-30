"""import array
arr = array.array('i', [])
print(arr, type(arr))
arr.append(10)
arr.append(20)
print(arr)
"""

'''
List:
1. use[] to create a list
2. List is mutable
3. List allows duplicate values
4. List is heterogeneous
5. List is indexed 
'''
'''
li = [12,25.4,6+5j,"Hello",12,25.4]
print(li, type(li))
print(li[3])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append(100)
print(li)
li.insert(2,"World")
print(li)
li.insert(-20,"Python")
print(li)
''' 
num = int(input("Enter a positive integer: 1234" \
""))
count = 0
while num > 0:
    digit = num % 10
    count += 1
    num = num // 10
print("Number of digits:", count)