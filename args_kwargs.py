def super_func(*args):
    print(args)
    return sum(args)

print (super_func(1,2,3,4,5))


# *args passes variable number of non-keyworded arguments list and on which operation of the list can be performed.
# **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.

def super_func(*args,**kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print (super_func(1,2,3,4,5,num1=5,num2=10))


#kwargs
def intro(**data):
    print ("\n Data type of arguments:",type(data))

    for key,value in data.items():
        print("{} is {}".format(key,value))

intro(FirstName='sita',Lastname="sharma",age="22",phone="1324134134")
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
