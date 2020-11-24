def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return True
arrayCheck([1,1,2,3,1])


def stringBits(mystring):

    result=" "

    for i in range(len(mystring)):
        if i%2==0:
            result=result +mystring[i]

    return result

    print(result)
