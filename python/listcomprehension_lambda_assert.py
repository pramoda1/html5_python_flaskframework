#----------------lambda-------------

#   lambda arguments: expression

#in python anonymos function is a function that is defined without a name
#it is defined by lamda

a= lambda x:x*2
print("double of 10 is ",a(10))


# using lambda with  "map"
# map fuction is apply the expression for each elements

numbers = [1,2,3,4,5]
squers = map(lambda x : x ** 2,numbers)
print(list(squers))


#using lambda with filter
#filter function is apply the condition and return the value for each element

number = [0,1,2,3,4,5,6,7,8,9,10]
even_number = filter(lambda x : x % 2 == 0,number)
print(list(even_number))

#using lambda with "sorted"
#sorted function is sort the elements

students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 72},
    {'name': 'Charlie', 'score': 95},
    {'name': 'David', 'score': 85}
]

sorted_students = sorted(students, key=lambda student: student['score'])

print(sorted_students)



#-----------------------------assert------------------------------

#     assert condition, message
#  Use assertions to catch logical errors during development.

def divide(a, b):
    assert b != 0, "The divisor 'b' cannot be zero"
    return a / b

print(divide(10, 2)) 
print(divide(10, 0)) 
