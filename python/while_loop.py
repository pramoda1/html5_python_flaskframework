# simple program

i=3
while i>0:
    print(i)
    i-=1

#sample2 with else
i=6
while i<10:
    print(i)
    i+=1
else:
    print("displayed sucessfully")

# n=6

'''the pattren is   
.....*
....***
...*****
..*******
.*********
***********
'''
'''1 5 1
   2 4 3
   3 3 5
   4 2 7
   5 1 9
   6 0 11 '''

#code
n=int(input("enthe number of row"))
i=1
while i<n:
    j=1
    while j< n-i:
        print(" ",end="")
        j=j+1
    j=1
    while j<= 2*i-1:
        print("*",end="")
        j+=1
    print()
    i+=1


# the pattren
'''
*******
 *****
  ***
   *
  ***
 *****
*******'''

#code
n=int(input("enter he  odd number of row"))
i=1
m=(n+1)/2

while i <= n:
    if i > m:
        b = n - i
        s = 2 * (i - m) + 1
    else:
        b = i - 1
        s = 2 * (m - i) + 1
    j = 1
    while j <= b:
        print(" ", end="")
        j += 1
    j = 1
    while j <= s:
        print("*", end="")
        j += 1
    print()
    i += 1

    #code
n=int(input("enter he  odd number of row"))
i=1
m=(n+1)/2

while i <= n:
    if i < m:
        b = m - i
        s = 2 * i -1
    else:
        b = i - m
        s = 2 * (n-i+1)-1
    j = 1
    while j <= b:
        print(".", end="")
        j += 1
    j = 1
    while j <= s:
        print("*", end="")
        j += 1
    print()
    i += 1