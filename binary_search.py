#in binary search all the values must be sorted
#Lower index and upper index bound
#Find min index = (lower+upper)/2
# if mid value = element we are searching i.e n, item found. if not then-->
#accordinng to situation mid value becomes upper/lower bound
#find new mid point.
# $search for the object

pos = -1
def search(list,n):

    l=0
    u = len(list)-1

    while l<=u: #lower bound is always smaller than upper bound
        mid = (l+u)//2 #// means integer division

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l =mid+1
            else:
                u =mid-1

    return False

list = [4,7,8,12,87,35,63,5365,3563,665]
n = 4
list.sort()

if search(list,n):
    print("Found at",pos+1)

else:
    print("Not found")
