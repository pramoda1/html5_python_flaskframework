def hello1():#function without return statement
    print("hello! I Love To code in pthon")

def hello2():# function using return
    return "hello! i love to code in python"
    #the return function is return back the contol to the caller

hello1()
print(hello2())


# example 2

def addition(x,y):
    print("the additionof two numbers is")
    return x+y

def subtraction(x,y):
    print("the subtraction of two numbers is")
    return x-y

def multiplication(x,y):
    print("the multiplication of two number is")
    return x*y

def menu():
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    ch=int(input("enter the option"))
    return ch

def caluclation():
    ch=menu()
    num1=int(input("enter the first number"))
    num2=int(input("enter the secand number"))
    if ch==1:
        print(addition(num1,num2))
    if ch==2:
        print(subtraction(num1,num2))
    if ch==3:
        print(multiplication(num1,num2))

caluclation()


#break statement

import random as r
rand_num=r.randrange(1,20)
print("number to be guessed :",rand_num)
i=1
while True:
    print("number guessed",i)
    if i==rand_num:
        print("the number gueseed sucessfully")
        break
    i+=1

#continue statements

for i in range(1,20):
    if(i%2 !=0):
        continue
    print(i)