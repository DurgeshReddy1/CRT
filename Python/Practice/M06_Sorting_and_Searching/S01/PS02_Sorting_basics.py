def Bubble_Sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
print(Bubble_Sort(list(map(int,input().split()))))

def Selection_Sort(nums):
    