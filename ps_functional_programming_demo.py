# funtional programming is passing functions as an argument to a function
# below hex,ord,sum are some functions
import re

print '\n\n'
print '1 ----------- with inbuilt functions ------------------------'


items = [2, 1, 3, 4, 5, 6, 7, 8]

temp = map(hex, items)
print temp
print


ascii = map(ord, 'peter pan')
print ascii


print
print map(sum, [[1,2,3], [5,6,7], [8,9,0]])   # for each element the sum method is called, so map loops internally



print '\n\n'
print '2 -------------  with user defined funtions  ----------------------'

ascii = [112, 101, 116, 101, 32, 112, 97, 110]


def tag_it(av):
    return 'ascii char="{}">{}</ascii>'.format(chr(av), av)

print map(tag_it, ascii)
print
print tag_it



print '\n\n'
print '3 -------------  using lambda ----------------------'

ascii = [112, 101, 116, 101, 32, 112, 97, 110]




print map(lambda av: 'ascii char="{}">{}</ascii>'.format(chr(av), av), ascii)
print
print tag_it


print '\n\n'
print '4 -------------  functional programmng using filter ----------------------'

items = range(1, 55)
print items
print
print filter(lambda n: n%7==0, items)   # print multiples of 7


print '\n\n'
print '5 -------------  functional programmng using filter and lambda for file operations ----------------------'

pattern = 'root'
mlines =filter(lambda line: re.search(pattern, line, re.I), open('resources/passwd.txt'))

for line in mlines:
    print line



