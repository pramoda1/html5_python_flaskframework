#function taking a arguments

def findmax(a,b):
    if a > b:
        return a
    else:
        return b
    
print("the maximum number between 10 and 20",findmax(10,20))

# defoult arguments
def one(name,msg="have a nice day"):
    print("hello",name,msg)

one("pramoda")
one("pramod","how r you")


#function with arbitory arguments
def sumAll(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print("the sum of all 1-5 integers",sumAll(1,2,3,4,5))