def my_func(param1='default'):
    print('My first python function!{}'.format(param1))

my_func()

#difference between returning something in function and printing

def hello():
    print("printing hello")

hello()

#returning helllo

def hello1():
    return "returning hello"

result=hello1()
print(result)


def addNum(num1,num2):
    return num1+num2

resultVar=addNum(2,3)
print ("addition of two number is",resultVar)


#check number if it is integer and add it

def addNumCheck(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry,I need integers"

result=addNumCheck(2,"3")
print(result)
