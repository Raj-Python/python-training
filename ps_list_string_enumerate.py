items = ['root', 'x', '0', '0', 'root','/root', '/bin/bash' ]


print "********  enumerate list  *******"
for index, value in enumerate(items):
    print "[{}] -> {}".format(index, value)


print
print "********  enumerate string  *******"
for index, value in enumerate('peter'):
    print "[{}] -> {}".format(index, value)
