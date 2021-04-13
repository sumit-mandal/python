#swapping
# compare 1st 2 value if 1st value is grater than 2nd then swap
# againn compare

def sort(nums):
    for i in range(len(nums)-1,0-1): #it means we are iterating lrt's say 5 to 1 with step size of -1
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5,3,8,6,7,2]
sort(nums)
print(nums)
