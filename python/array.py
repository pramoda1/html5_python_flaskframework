arr=[10,20,30,40,50,60,]
print(arr[1])
print(arr[-1])
print(arr[1:4])
print(arr[-1:-4])

#add the element into the array
brands=["apple","banana","straberry","pomogranate","kivi","grapse"]
print(brands)
num_attributes=len(brands)
print(num_attributes)
brands.append("sapota")
print(brands)

#removing elements in array
colors=["green","blue","white","red","black","pink","purple"]
print(colors)
colors.remove("white")
print(colors)
colors.pop(0)
print(colors)


#modifieng the array
colors[2]="white"
print(colors)

#concatinate the two array using + operator
con=colors+brands
print(con)

#slicing an array
print(colors[2])
print(colors[1:])
print(colors[:3])
print(colors[-3])


#declaring two domensional array and defining
mult=[[1,2],[3,4],[5,6],[7,8]]
print(mult)
print(mult[2])
print(mult[1][0])