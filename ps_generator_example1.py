'''
	1. Looks like a normal function
	2. should use yeild keyword atleast  once
    3. generators return iterators
    4. Generators resume execution
    5. can maintain state in local variables
    6. complex control flow
    7. Lazy evaluation
'''


#### Example 1
def gen123():
    yield 1
    yield 2
    yield 3

def main_func():
    g = gen123()
    print type(g)
    print next(g)
    print next(g)
    print next(g)
    print next(g) #since there is no 4th element it will throw an exception


if __name__ == '__main__':
    main_func()