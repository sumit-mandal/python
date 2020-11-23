s='django'

print(s[0])

print(s[0:4])

print('reversing',s[::-1])

l=[3,7,[1,4,'hello']]

l[2][2]='goodbye'
print("reassign hello to goodbye",l)

#prob-3

d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}

print("grabbing hello from d1:" ,d1['simple_key'])
print("grabbing hello from d2:" ,d2['k1']['k2'])
print("grabbing hello from d3:" ,d3['k1'][0]['nest_key'][1][0])


#prob-3
mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

#prob4

# age=4
# name="sammy"

var4="hello my dog's name is {name} and he is {age} years old ".format(age=4,name="sammy")
print(var4)
