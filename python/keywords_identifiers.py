#True False
print(5==5)

print(5>5)
#none
print(None==1)
print(None==None)

def a_void_function():
    a=1
    b=2
    c=a+b
    return(c)

x=a_void_function()
print(x)

#and,or,not
print(True and False)
print(True or False)
print(not False)
print(True and True)
print(False and False)

# as
import math as mt
print(mt.cos(mt.pi))


#assert
assert 5 >4

#break
for i in range(1,11):
    if i==5:
        break
    print(i)

#continue
for i in range(1,11):
    if i==5:
        continue
    print(i)

#class
class example:
    def function1(self):
        print("function1 is exucuting")
    def function2(self):
        print("function2 is executing")

ob1=example()
ob1.function1()
ob1.function2()


#def
class example2:
    def function3(self):
        pass
ob2=example2()
ob2.function3()



'''# del
a=10
print(a)
del a 
print(a)'''


#if..elif..else

num=2
if num==1:
    print("one")
elif num==2:
    print("two")
else:
    print("somthing else")


#try...raise...catch...finally

try:
    x=9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("division cannot be perform")
finally:
    print("execution succesfully")


#for
for i in range(1,10):
    print(i)


#from...import
import math
from math import cos
print(cos(10))

#global

'''class example3:
    globalvar=10
    def read(self):
        print(glabalvar)
    def write(self):
        global globalvar
        globalvar=5
        print(globalvar)
    def read1(self):
        globalvar=15
        print(globalvar)

ob=example3()
ob.read()
ob.write()
ob.read1()'''

# in
arr=[1,2,3,4,5,6]
print(4 in arr)
print(7 in arr)
print(44 not in arr)

#is 
print(True is True)

#lambda
a=lambda x:x*2
for i in range(1,6):
    print(a(i))


#nonlocal


