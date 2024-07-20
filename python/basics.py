# namespce (also known as identifier) and id is a get the memory addres of the value
a=2
print('id(2)',id(a))
print(id(2))

#scope
def outerfuction():
    global a
    a=20
    def innerfuction():
        global a
        a=30
        print(a)
    innerfuction()
    print(a)

a=10
print(a)
outerfuction()
print(a)

# global and local variable in diffrent name
x="global"
def outerfuction():
    global x
    y="local"
    x=x*2
    print(x)
    print(y)

print(x)
outerfuction()
print(x)

#global and local variable in same name

a=5
def outer():
    a=10
    print(a)

print(a)
outer()
print(a)

# creating and intilizing the non local variables

def outer():
    x="local"
    def inner():
        nonlocal x
        x="non local"
        print(x)
    inner()
    print(x)
outer()


