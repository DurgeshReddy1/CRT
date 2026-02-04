'''
Numpy: 
    Numpy---> Numerical Python
    Mainly it provides the efficient arrays
'''
import numpy as np
arr = np.array([10,20,30,40,50])
print("Array elements are: ", arr)
print(np.max(arr))    
print(np.min(arr))      
print(np.mean(arr))  
print(np.sum(arr)) 
print(np.zeros(5))
print(np.ones(5))
print("Even numbers: ", np.arange(2,10,2))
print("Odd numbers: ", np.arange(1,10,2))

n = int(input("Enter the size: "))
ele = list(map(int, input("Enter the elements: ").split()))
print("Array elements are: ", np.array(ele))