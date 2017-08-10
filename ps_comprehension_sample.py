from pprint import pprint as pp


print '\n\n'
print '1 ----------  set comprehension  -------------------------'
print {hex(i) for i in range (1,6)} # set comprehension

print '\n\n'
print '2 -------------  dict comprehension  ----------------------'
print {i: hex(i) for i in range(1,6)} # dict comprehension


print '\n\n'
print '3 -------------  dict comprehension ----------------------'


d = {line.split(':')[0] : line.rstrip().split(':')[1:] for line in open('resources/data1.txt')}
pp(d)






