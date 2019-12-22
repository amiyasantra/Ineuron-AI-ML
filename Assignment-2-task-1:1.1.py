#1.1 Write a Python Program to implemPython's built-in function reduce 

def my_reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value
mylist=[2,3,4,5]
my_reduce(lambda x,y:x+y,mylist)

