# a is 2d marix
a=[[1,2,3,4,5],
   [1,2,3,4,5],
   [1,2,3,4,5]]

# b is nested list but not matrix becouse the number of elements is diffrent

b=[[1,2,3,4,5],
   [1,2,3,4],
   [1,2,3,4,5]]

print(a)
print(b)

# create a dynomic matrix using for loop
# Define the dimensions of the matrix
rows = 3
cols = 4

# Create an empty matrix
matrix = []

# Populate the matrix using nested for loops
for i in range(rows):
    # Create a new row
    row = []
    for j in range(cols):
        # Append a value to the row (e.g., i * j)
        row.append(i * j)
    # Append the row to the matrix
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)

#Acessing the atrix elements
print(matrix[1][2])


# chenge the elements of matrix in python
matrix[1][2]=100
print(matrix[1][2])

matrix[0]=[1,1,1,1]
print(matrix[0])

