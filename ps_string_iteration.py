'''
iteration syntax :-

for temp in iter-obj:
    pass
'''


print '*********** iteration ***********'

s = 'this is a sample string in python'

for item in s:
    if item not in 'aeiou ':  # membership test operator
        print "{}: {}".format(item, ord(item))
    else:
        print '**'



print '1. -----------------------------------'


s = 'this is a sample string'
print 'sam' in s
print 's a' in s
print 'zee' not in s


print '2. -----------------------------------'

items = range(22)
print items
print 12 in items


