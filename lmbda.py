#lambda Expression



#filter function

myList=[1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0

evens=filter(even_bool,myList)
print("using define function:",list(evens))


evens=filter(lambda num:num%2==0,myList)
print("Using lambda function:",list(evens))

print('x' in [1,2,3,'x'])
