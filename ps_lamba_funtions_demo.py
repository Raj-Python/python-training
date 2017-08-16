#syntax
#lambda arg1, arg2, ........: expression
# should not be more than a single line
# used for callback
# map should have iteratable object

print '\n\n'
print '1 -------------  using lambda ----------------------'

power = lambda x,n:x*n

print power
print power(3,4)



print '\n\n'
print '2 -------------  using lambda with multiple arguments ----------------------'

xs = [2, 4, 6, 8]
ns = [1, 2, 3, 4]

print map(lambda x,n : x ** n, xs, ns)


