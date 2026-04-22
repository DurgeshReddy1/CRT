'''
Optimization: It is the process of modifying the code to get more efficent.
Efficeint:
1) To reduce time complexity
2) To reduce space complexity
3) To reduce memory usage
4) To avoid un-necessary operations

'''
a = [10,20,30,40,50]
target = 30
for i in range(len(a)):
    if a[i] == target:
        print("Ele found")

a = [10,20,30,40,50]
if 30 in a:
    print("Ele found")

#Write the python code to print the sum of the ele in list
a=[10,20,30,40,50]
sum = 0
for i in range(len(a)):
       sum += a[i]
print(sum)

a=[10,20,30,40,50]
print(sum(a))

#Two Sum
a=[2,7,11,15]
target = 9
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print(i,j)     #O(n^2)--> Brute force

a=[2,7,11,15]
target = 9
d={}
for i in range(len(a)):
    res = target - a[i]
    if res in d:
        print(d[res], i) 
    d[a[res]] = i          #O(n)--> Optimized Solution

'''
Common ways to get OPtimization:
1) Reducing the time complexity optimization (Ex:O(n^2) to O(n))
2)Hashing(use set/dict)
3)Avoid un-necessary calculations
4)Use built-in functions
5)List comprehension Optimization
'''
a=[]
for i in range(10):
    a.append(i*i)
print(a)

a=[i*i for i in range(10)]
print(a)

#Write a python code to print the max ele using for loop?
