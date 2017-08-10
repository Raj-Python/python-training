# regular expression are case sensitive
# regular exp matches only once in a line
# regular exp are case sensitive


import re

print '\n\n'
print '1 -------------- match the pattern ---------------------'
s = 'the python and the perl scripting'

pattern = 'P.+?N'
m = re.search(pattern, s , re.I)

if m:
    print 'match :', m.group()
else:
    print 'failed to match'




print '\n\n'
print '2 --------------  except the match pattern  ---------------------'
s = 'the python and the perl scripting'

pattern = 'P.+?N'
m = re.search(pattern, s , re.I)

if m:
    print 'match :', m.group()
    before  = s[:m.start()]
    after = s[m.end():]
    print 'before : |{}|'.format(before)
    print 'after : |{}|'.format(after)
else:
    print 'failed to match'



print '\n\n'
print '3 --------------  matching multiple times  ---------------------'
s = 'the python and the perl scripting'

pattern = 'P.+?N'
for  m in re.finditer(pattern, s, re.I):
    print m.group()
    print m.span()
    print

print re.findall(pattern, s , re.I)  # list of match string

