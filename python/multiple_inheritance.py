#multiple inheritance syntax
class car:
    pass
class bike:
    pass
class veichele(car,bike):
    pass

#example 1

class abc:
    def add(self):
        self.a=10
        self.b=20
        print("the addition of two numbers",self.a+self.b)

class xyz:
    def sub(self):
        self.c=10
        self.d=20
        print(self.d-self.c)

class pqr(abc,xyz):
    def __init__(self):
        #super().__init__()
        pass
    def mul(self):
        self.sub()
        self.add()
        print("the multiplication two numbers",self.d*self.a)
        

#create a instances
object=pqr()
object.mul()


    