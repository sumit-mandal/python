#python scope follows legb rule

# local-names assigned in any way within a function(def or lambda),and not declare global in the  function

# Encloding function locals-name in local scope of any and all enclosing function,from inner to outer

# global--name assigned at the top level module file,or declared global in a def with in a file

# builtin-name preassigned in the built-in names module:open,range,SyntaxError,..

x=25

def my_func():
    x=50
    return x


"""
print("global function called:",x)
print("Global function is redefined to local :",my_func())

"""

my_func()
print(x)


#local

lambda x:x**2

#Enclosing function locals
name='This is a global name'

def greet():
    # name="sammy"

    def hello():
        print("hello "+name)

    hello()
greet()
