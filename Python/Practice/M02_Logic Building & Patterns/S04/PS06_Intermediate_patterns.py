'''
li = [1,2,3,4,5] 
#Output: [2, 4, 6, 8, 10]
res = []
for i in li:
    res.append(i*2)
print(res)

'''
'''
#Input: [1,2,3,4,5]
#Output: [2, 4]
li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

print([i for i in li if i % 2 == 0])
'''
#['a', 'b', 'c'] ==> "abc"
'''
li1 = ['a', 'b', 'c']
res = ""
for i in li1:
    res += i
print(res)

print("".join(li1))
'''

'''
Intermediate patterns
1. Pyramid pattern
    n = 4
    Output:
         *
        * *
       * * *
      * * * *
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

'''
2. Inverted Pyramid
    n = 4
    Output:
        
'''