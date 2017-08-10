'''

indexing table
=============

0   1   2   3 +ve

p   e   r   l

-4 -3   -2 -1 -ve

'''


print '*********** indexing ***********'

s = 'perl'
print s[0]
print s[1]
print s[2]
print s[3]


print


print s[-1]
print s[-2]
print s[-3]
print s[-4]




print '*********** Slicing ***********'

s = 'perlandpython'

print s[0:4]
print s[3:7]
print s[-6:]
print s[:]
print s[1:-1]
print s[-6:-4]
print s[::1]
print s[::-1] # reverses the string
print s[::-1] == s  # checks for palindrome or not
print s[::2]

print '==============================='

s = 'this is a sample string'
s2 = s.replace('sample','simple')
print s
print s2




