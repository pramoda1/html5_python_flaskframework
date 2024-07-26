try:
    a="hi"
    b=int(a)
except:
    print("exception is caught..")

#caughing specific exception

try:
    a=10
    b=0
    c=a/b

except ZeroDivisionError as e:
    print("the exception is",e)

#the exception  can be raised also
try:
    raise ZeroDivisionError 
except:
    print("the exception is accur")


#try.....finaly
try:
    raise ZeroDivisionError
    print("the try block")
    raise TabError
except:
    print("the error is  accur")
finally:
    print("the finally block")


#example 2

try:
    a=int(input(" enter the number"))
    b=int(input("enter the number"))
    if(a>b):
        raise TypeError
    c=a/b
    print(c)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
finally:
    print("complete")

