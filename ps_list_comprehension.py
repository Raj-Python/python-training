from  pprint import pprint as pp

items = [2, 1, 3, 4, 5, 6, ]
temp2 = [bin(item) for item in items]  # list comprehension
print temp2


print '\n\n'
print '1 -----------------------------------'

temp2 = [i**i for i in items]
print temp2

print '\n\n'
print '2 -----------------------------------'
print [ord(char) for char in 'peter pan']

print '\n\n'
print '3 -----------------------------------'
items = [2, 1, 3, 4, 5, 6, ]
print [i for i in items if i%2]


print '\n\n'
print '4 -----------------------------------'
print [c.upper() if i%2 == 0 else c for i, c in enumerate('peter pan')]


print '\n\n'
print '5 -----------------------------------'

ul = [line.split(':')[0].upper() for line in open('resources/passwd.txt') if line.startswith('a')]
pp(ul)


print '\n\n'
print '6 -----------------------------------'

content = [line.rstrip().split(':') for line in open('resources/passwd.txt') if line.endswith('bash\n')]

heading = ['login', 'password', 'uid', 'gid', 'gecos', 'home', 'shell' ]

for user_info in content:
    for name, value  in zip(heading, user_info):
        print  "{:>16} : {}".format(name, value)
    print

#print content
pp(content, width=100)


