#Using the property function in Python involves defining a managed attribute with getter, setter, 
# and deleter methods.  You can use the property function directly or
#  with decorators for more readable and concise code.

#Using the property function without decorators

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)

# Usage
p = Person("Alice")
print(p.name)        # Output: Alice (calls get_name)
p.name = "Bob"       # calls set_name
print(p.name)        # Output: Bob (calls get_name)
del p.name           # calls del_name


#Using the property function with decorators

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @name.deleter
    def name(self):
        del self._name

# Usage
p = Person("Alice")
print(p.name)        # Output: Alice (calls the getter)
p.name = "Bob"       # calls the setter
print(p.name)        # Output: Bob (calls the getter)
del p.name           # calls the deleter
