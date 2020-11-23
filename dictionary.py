my_stuff={"key1":"value",'key2':'value2','key3':{'123':[1,2,3]}}
print("Key 1 is :",my_stuff["key1"])

my_stuff2={"key1":"123",'key2':"value2",'key3':{'123':[1,2,'grabme']}}
print("Here 2 is index number:",my_stuff2['key3']['123'][2])

my_stuff3={'lunch':'Pizza','bfast':'macchli'}
my_stuff3['lunch']='burger'
my_stuff3['dinner']='pasta'

print('updated dictionary:',my_stuff3)
