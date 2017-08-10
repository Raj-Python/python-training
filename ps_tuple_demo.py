
print '\n\n'
print '1 ---------  tuple sample  --------------------------'

t = (1, 2.2, 4+3j, 'pam', 5.0)
print t[-3]
print t[:-3]
print
for item in t:
    print item



print '\n\n'
print '2 ---------  parallel assignment  --------------------------'

name, age, gender =  t = 'sam', '3', 'male'
print t
print name
print gender


print '\n\n'
print '3 ---------  tuple to use to return more than one values --------------------------'
print divmod(5.0, 2)
q, r = divmod(5.0, 2)
print q
print r



print '\n\n'
print '4 ---------  tuple to use to return more than one values --------------------------'
def sqr_and_cube(n):
    return n**2, n**3


print sqr_and_cube(5)


