set1={1,2,34,4,5}
print(set1)

#mixed data type
set2={1,2,"abcd",(1,2,3,4)}
print(set2)

# operation on sets
set3={11,22,33,44,55}
# print(set3[2]) # error 

# add on element
set3.add(66)
print(set3)

# add multiple element
set3.update([1,2,3,4])
print(set3)

# add list and set

set3.update([6,7,89],{34,67})
print(set3)

# discard and remove 
set3.remove(11)
print(set3)
set3.discard(22)
print(set3)

# using pop

print(set3.pop())
print(set3)

# set operation - union
se={1,2,3,4,5}
se1={1,6,7,8,9,0}
print(se,se1)

# operation

print(se | se1)
print(se1 | se)
print(se.union(se1))
print(se1.union(se))

# intersection 
print(se & se1)
print(se1 & se)
print(se.intersection(se1))
print(se1.intersection(se))

# set difference
print(se - se1)
print(se1 - se)
print(se. difference(se1))
print(se1.difference(se))

# symetric difference
print(se ^ se1)
print(se1 ^ se)
print(se.symmetric_difference(se1))
print(se1.symmetric_difference(se))

# membership 
print(2 in se)
print( 2 not in se)

#iterate
for i in set("pramod"):
    print(i)

# built in fuction
print(min(se))
print(len(se))
