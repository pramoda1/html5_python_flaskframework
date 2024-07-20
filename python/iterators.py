#iterators are implimented in loops generators and caprehensions 
# iterators nothing but object
#iterators return the data one at a time during our iteration


#The __iter__() method, which is called on the collection object, returns an iterator from it. Then, 
# the __next__() method is used to get the next value from the iterator

our_list=[1,2,3,4,5]
our_iterator=iter(our_list)
print(next(our_iterator))
# using object
print(our_iterator.__next__())
print(next(our_iterator))
print(next(our_iterator))
print(next(our_iterator))

# create a coustom iterator

class pow_of_two:
    ''' clss implemention in iter and next methods'''
    def __init__(self, max):
        self.max=max

    def __iter__(self):
        self.n=0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
    
print(pow_of_two.__doc__)
a=pow_of_two(4)
i=iter(a)
print(next(i))        
print(next(i))
print(next(i))
print(next(i))
print(next(i))


#infinate iterators
class infinateiterators:
    ''' clss implemention in iter and next methods in infinate iterators '''
    

    def __iter__(self):
        self.num=1
        return self
    
    def __next__(self):
       num=self.num
       self.num+=1
       return num
    
print(infinateiterators.__doc__)
i=iter(a)
print(next(i))        
print(next(i))
print(next(i))
print(next(i))
print(next(i))
