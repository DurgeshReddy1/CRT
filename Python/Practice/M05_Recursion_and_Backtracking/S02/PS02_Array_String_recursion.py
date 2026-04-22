def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
    return s
print(Array_sum([1, 2, 3, 4, 5]))  # Output: 15

def Array_sum(nums, i):
    if i == 0:
        return 0
    return nums[i-1] + Array_sum(nums, i-1)

print(Array_sum([1, 2, 3, 4, 5], 5))  # Output: 15

def Array_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + Array_sum(nums[:-1])

print(Array_sum([1, 2, 3, 4, 5]))  # Output: 15

li = [12,0,45,78,6,9]
print(li)
print(li[-1])  # Output: 9

#Reverse Array
def Reverse_Array(nums):
    if i >= j:
        return nums
    nums[i], nums[j] = nums[j], nums[i]
    return Reverse_Array(nums, i+1, j-1)

print(Reverse_Array([1, 2, 3, 4, 5],0,4))  # Output: [5, 4, 3, 2, 1]

def Reverse_String(st):
    if st == "":
        return ""
    return st[-1] + Reverse_String(st[:-1])
print(Reverse_String("Hello"))  # Output: "olleH"

def is_pallindrone(st):
    