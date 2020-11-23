d={"sam":1,"frank":2,"dan":3}

for k in d:
    print(k)
    print(d[k])


#usually we have tuples inside a list

mypairs=[(1,2),(3,4),(5,6)]

for item in mypairs:
    print("printing all the  items:",item)

#tuple unpacking

for(tup1,tup2) in mypairs:
    print("Printing second tuples",tup2)
    print("printing first tuples",tup1)



#while loops

i=1

while i<5:
    print("i is :{}".format(i))
    i=i+1



#range function
k=list(range(5))
print("range is:",k)

l=list(range(0,20,2))
print("We'll have gap of two :",l)

for item in range(10):
    print(item)



#list  comprehension

x=[1,2,3,4]

out=[]

for num in x:
    out.append(num**2)

print("noraml method:",out)


#comprehension method\

b=[1,2,3,4]
out=[num**2 for num in x]
print("Commprehnsion method:",out)
