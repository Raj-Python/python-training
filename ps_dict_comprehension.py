from math import sqrt


''' syntax for dict comprehension with filtering predicate is   
                                                                
    [expr(item) for item in iterable if predicate(item) ]       
'''


def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True



def printPrime():
   print("Prime numbers are")
   print([x for x in range(101) if is_prime(x)])

#if is_prime(x) in the above function is a filtering predicate which is optional in comprehension




if __name__ == '__main__':
    printPrime()