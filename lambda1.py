
my_list = [1,2,3]

def multiply_by2(item):
    return item*2

print("using map function",list(map(multiply_by2,my_list)))

# -----------------------------------------------------------

#using lambda

print(list(map(lambda item : item*2,my_list)))
