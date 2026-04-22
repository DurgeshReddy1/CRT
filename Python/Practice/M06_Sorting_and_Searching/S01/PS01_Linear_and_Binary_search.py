'''
1. Sequential Search (Linear Search)
best case ==> O(1) 
Average case ==> O(n)
Worst case ==> O(n)

2. Interval Search
best case ==> O(1)
Average case ==> O(log n)
Worst case ==> O(log n)
'''

def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
  
nums = list(map(int,input().split()))
target = int(input())
print(linear_search(nums,target))

def binary_search(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
nums = list(map(int,input().split()))
target = int(input())
print(binary_search(nums,target))   