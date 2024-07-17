class maths:
    def __init__(self,a,b):
        print("the constrocter is excuting")
        self.a=a
        self.b=b

    def add(self):
        print("the addition of two numbers",self.a+self.b)
        

obj=maths(10,20)
obj.add()