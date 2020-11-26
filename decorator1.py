#calling function within itself is known as decorattor
# Decorators allow us to wrap another
# function in order to extend the behavior of wrapped function,
# without permanently modifying it.

# In Decorators, functions are taken as the argument into
# another function and then called inside the wrapper function.

def new_decorator(func):


    def wrap_func():
        print("Code here before executing func")
        func()
        print("func has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator!")

# func_needs_decorator=new_decorator(func_needs_decorator)
func_needs_decorator()
