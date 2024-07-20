tuple1=()
print()

tuple1=(1,2,3,4,5)
print(tuple1)

tuple2=(1,"abcd",4.3)
print(tuple2)

#nested tuple
tuple3=("points",[1,2,3,4],(6,7,89))
print(tuple3)

#tuple unpacking
tu= 1,2,3,4,5
emp1,emp2,emp3,emp4,emp5=tu
print(emp1)

# accesing the tuples values
print(tu[1])

#tuple elements are immutable
#tu[2]='x'
print(tu)

#slicing tuple elements
print(tu[1:3])

# concatination 
print(tu+tuple2)

#operations
tup=1,2,34,5
print(tup)
del tup
#print(tup)

print([tu.count('1')])
print(tu.index(1))


#tuple operations
tupl=1,2,3,4,5,6
print('1' in tupl)
print('1'not in tupl)
print('1' is tupl)
print('1' is not tupl)

#iteration through tuples
for i in tupl:
    print("numbers is -->",i)

#builtin function in tuple

print(max(tupl))
print(min(tupl))
print(sorted(tupl))
print(len(tupl))