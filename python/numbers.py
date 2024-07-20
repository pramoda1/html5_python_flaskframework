# int numbers
a=10
print(type(a))
print(isinstance(a,int))
print(isinstance(a,float))
print(isinstance(a,complex))

# float numbes
b=1.2
print(type(b))
print(isinstance(b,int))
print(isinstance(b,float))
print(isinstance(b,complex))

# complex number
c=10+3j
print(type(c))
print(isinstance(c,int))
print(isinstance(c,float))
print(isinstance(c,complex))

# form
print(0b1101) # binary form
print(0xab) #hex
print(0o23) #octet

# type conversion
print(int(20.5))
print(int(-20.6))
print(float(10))

#python decimal
'''num=1.2+1.8
print(num)
from decimal import Decimal as d
print(d('1.2')+d('1.8'))'''

#from fractions import Fraction as F
#print(F(1.5))

#python  math module
import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.factorial(2))
print(math.exp(10))

#random
import random
print("the random number-->",random.randrange(1,10))
print("the random number-->",random.randrange(1,10))
print("the random number-->",random.randrange(1,10))
print("the random number-->",random.randrange(1,10))
day=[1,2,3,4,5,6,7]
print(random.choice(day))
random.shuffle(day)
print(day)
print(random.random())