#creating a class and objects in python

class mybird:

    def __init__(self) :
        print("my bird class constructor is excuting..")

    def whattype(self):
        print("i am bird..")

    def canswim(self):
        print("i can swim")

class myparrot:
    #class attributes
    spacies="bird"
    #instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def cansing(self):
        return"{} can sing {}....".format(self.name)
    
    #my parrot class inheritang the attributes fromm the mybird class
class mypenguin(mybird):
    def __init__(self):
        super().__init__()
        print("penguin is readt")
        
    def whoisthis(self):
        print(" i am penguin")
        
    def canrun(self):
        print("i can run faster")

#instantiate the parrot class

m1=myparrot("myparrot1",10)
m2=myparrot("myparrot2",20)

# acess the class attibutes
print("mp1 is {}".format(m1.__class__.spacies))
print("mmp2 is {} ".format(m2.__class__.spacies))

#acess the instance attributes
print("{} is {} year of age ".format(m1.name,m1.age))
print("{} is {} year of age ".format(m2.name,m2.age))

#accesing the child class attributes inheritance
pg1= mypenguin()
pg1.whoisthis()
pg1.canswim()
pg1.canrun()

#data encapsulation 

class personalcomputer:
    def __init__(self) :
        self.maxcomputerprice=2000

    def mysell(self):
        print("sellig price :{}".format(self.maxcomputerprice))
    
    def setmaxcomputerprice(self,price):
        self.maxcomputerprice=price

pc=personalcomputer()
pc.mysell()

# change the price

pc.maxcomputerprice=30000
pc.mysell()

#using setter fuction

pc.setmaxcomputerprice(40000)
pc.mysell()