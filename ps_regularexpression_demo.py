# regular expression are case sensitive
# regular exp matches only once in a line
# regular exp are case sensitive


import re
from fileinput import input

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



print '\n\n'
print '4 --------------  find and replace  ---------------------'
s = 'root:x:0:0:root:.root:/bin/bash'

pattern = ':'
replacement = ','
s2 = re.sub(pattern, replacement, s)
print s2
print


s3 = re.sub('[AEIOU]', '*', s, flags=re.I)
print s3




print '\n\n'
print '5 --------------  find and replace from a file  ---------------------'

for line in input('resources/passwd2.txt', inplace=True, backup='.bak'):
    print re.sub(':', ',', line)






print '\n\n'
print '6 --------------  split version of regex  ---------------------'


s = 'root,x:0;0 root,/root,/bin/bash'
items = re.split('[,:]', s)
print items
items = re.split('[,:;]', s)
print items
items = re.split('[,:;\s/]', s)
print items