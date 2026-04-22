''' 
a=set([10,20,30,40,50])
print(a)
a.add(78)
a.add(50)
print(a)
a.remove(20)
print(a)
a.discard(30)
print(a)
b = set([40,50,60,70,80])
print(b)    
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


#3)Accessing of tuple:
t=(1,2,3,45,50)
#t[0]=10 
print(t[0])  #error because tuple is immutable

#4) Concatenation of tuple
t = (1,2,3,45,50)
t2 = (2,3,567,8)
print(t+t2)  #concatenation of tuple

#5) Repetition of tuple
t = (1,2,3,45,50)
print(t*3)  

#6) Nesting of tuple
t = (1,2,3,45,50)       
t2 = (2,3,567,8)
print((t,t2))  

#7) Slicing of tuple
t = (1,2,3,45,50)
print(t[1:])  
print(t[0:3])  

#8) Deleting of tuple
t = (1,2,3,45,50)
del t
print(t) 

#9) Leetcode problem on tuple (349,657)
'''
#1Dictionary- store data in key-value pair
#2) Creation (().dict())
d={"name":"Durgesh","age":19}
print(d)
d1=dict(name="Durgesh",age=19)
print(d1)

#3) Accessing of dictionary
d={"name":"Durgesh","age":19}
print(d.get("name"))
print(d.keys())
print(d.values())

#4) Adding & Updating of dictionary
d={"name":"Durgesh","age":19}
d['phone']=1234567890
print(d)    
d['name']="Durgesh"
print(d)

#5) Removing dict items (del.pop(),popitem().clear())
d={"name":"Durgesh","age":19}
del d['age']
print(d.pop("name"))
print(d.popitem())
d.clear()
print(d)

#6) Leetcode problem on dictionary (1,242)