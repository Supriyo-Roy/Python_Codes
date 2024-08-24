from array import *
a1 = array('i',[22,33,44,55,66,22])
a1.append(400)
for x in a1:
    print(x,end=" ") #by default end = \n(new line) you can override
print(a1.count(22))    