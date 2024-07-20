# implict conversion
num_int=123
num_float=12.3
print(type(num_float))
print(type(num_int))
num_new=num_int+num_float
print(num_new)
print(type(num_new))

#problem of implict
numstr="pramod"
num=12
print(type(numstr))
print(type(num))
# numn=numstr+num
#print(numn) implicit conversion not working

#explicit type conversion
num1=123
num2='123'
print(type(num1))
print(type(num2))
num2=int(num2) #type conversion
print( "ofter conversion",type(num2))
