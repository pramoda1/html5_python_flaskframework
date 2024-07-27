class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the + operator
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
         return Point(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        # Overloading the repr method for easy printing
        return f"Point({self.x}, {self.y})"

# Create two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Add the points using the overloaded + operator
p3 = p1 + p2
p3 =p1-p2

# Print the result
print(p3)  

''' __add__(self, other): Addition (+)
__sub__(self, other): Subtraction (-)
__mul__(self, other): Multiplication (*)
__truediv__(self, other): True division (/)
__floordiv__(self, other): Floor division (//)
__mod__(self, other): Modulo (%)
__pow__(self, other): Exponentiation (**)
__eq__(self, other): Equality comparison (==)
__ne__(self, other): Inequality comparison (!=)
__lt__(self, other): Less than (<)
__le__(self, other): Less than or equal to (<=)
__gt__(self, other): Greater than (>)
__ge__(self, other): Greater than or equal to (>=)'''
