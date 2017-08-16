from sys import stderr, exc_info
from traceback import print_tb



print '\n\n'
print '1 --------------  funtion where exception is printed to the error device  ---------------------'


def power(x,n=0):
    return x ** n

try:
    print power(4, 3)
    print power(4)
except TypeError as err:
    print >>stderr, 'blah blah ....'    # prints on the error device




print '\n\n'
print '2 --------------  function to print entire exception stacktrace  ---------------------'


def power2(x, n):
    return x ** n


try:
    print power2(4, 3)
    print power2(4)
except TypeError as err:
    print err
    print_tb(exc_info()[-1])  # prints entire stack trace




print '\n\n'
print '3 --------------  function with multiple args (*args) ---------------------'

def demo(*args):   # multiple args will become a tuple
    print args


demo()
demo(100)
demo('pete')
demo(1, 2.2, 'iii', 4.4, 5.0)
items = [1, 2, 3, 4, 5]
demo(items)                 # list will become the first element of the tuple.


a = (1, 2, 3.3, 4.0, 5.0)
b = [1, 2, 3.3, 4.0, 5.0]
demo(a)  # passing tuple itself
demo(*a) # passing only contents of a tuple or list or string

demo(*'peter') # passing contents of a string
demo(b)
demo(*b)   # passing only contents of a  list



print '\n\n'
print '4 --------------  *args should always be the last argument ---------------------'



def demo(a, b, *args):
    print a
    print b
    print args


demo(1,2)
demo(1,2,3,4,5)














