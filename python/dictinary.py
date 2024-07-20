# dictinary have key and value enclosed wit cury braces
dic={1:"a",2:"b",3:"c",4:"d"}
print(dic)

# print using key  value
print(dic[1])

# using get method
print(dic.get(1))

 # update the value using key
dic[1]='e'
print(dic)

# adding value 
dic[5]="f"
print(dic)

# creating new dictinary
dic1={1:"a",2:"b",3:"c",4:"d"}
print(dic1)

#remove the partcular item using pop
print(dic1.pop(4))
print(dic1)

# remove the orbitary item
print(dic1.popitem())
print(dic1)

#delete the particular item using key value
del dic1[1]
print(dic1)

#slicing
#print(dic1[1:3])
#print(dic1[:3])

#membership
print("a" in dic1)
print("a" not in dic1)

#using key
print(3 in dic)

#iterating through
for i in dic1:
    print(dic1[i])

# built in function

print(len(dic1))
print(sorted(dic1))



