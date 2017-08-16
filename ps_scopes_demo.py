n = 10 # global

def demo():
    n = 'pip' #local
    print globals()['n']  # global variable
    print n

demo()
print n