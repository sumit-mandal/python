#tutorials point
def printme(str):
    "This prints a passed string into the function"
    print (str)
    return

printme("I'm first call to user defined function")
printme("I'm second call to user defined function")


def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")
