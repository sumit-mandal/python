try:
    f=open('simple.txt','r')
    f.write("test write to simple text")
except IOError:
    print("Error: could not find file or read data")
else:
    print("success!")
    f.close()

#finally keyword always works

try:
    f=open('simple.txt','r')
    f.write("test write to simple text")
except IOError:
    print("Error: could not find file or read data")
finally:
    print("I always work no matter what")
