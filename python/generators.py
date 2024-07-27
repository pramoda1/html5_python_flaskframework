'''Generators in Python are a type of iterable, like lists or tuples, 
but they generate items one at a time and only when asked. This is known as lazy evaluation. 
Generators are particularly useful when working with large datasets or streams of data,
 as they allow you to generate data on the fly without storing the entire dataset in memory.'''

class RangeGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self._generate()

    def _generate(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

# Create an instance of RangeGenerator
range_gen = RangeGenerator(1, 5)

# Get an iterator from the generator
iterator = iter(range_gen)

# Use next() on the iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2

# Use the generator in a for loop

# Output:
# 3
# 4
