items = [] # list()
print items
print len(items)
print type(items)



items = [2.2, 'pam', 3.3, 'andy', .3, 'eva', '1.2']
items.append('intuit')
items.insert(0,'bangalore')

print items


print('****** delete *****')

value = items.pop()  # deletes the last item
print items
print
print('---------------------------')

value = items.pop(-4) # deletes last fourth item
print items
print

print('---------------------------')

items = [2.2, 'pam', 3.3, 'pam', .3, 'eva', 1.2, 'pam', 'pam']
item = 'pam'

while item in items:
        items.remove(item)

print items


print('**** list concat *****')
vows = ['a', 'e', 'i']
others = [1, 2, 3]
vows.extend(others)   # extend the current list
print vows

print('---------------------------')

vows = ['a', 'e', 'i']
others = [1, 2, 3]
newer = vows + others # create a new lis of the two
print newer

print('---------------------------')
vows = ['a', 'e', 'i']
content = vows * 3
print content
print
print set(content)
print
print list(set(content))



print
print

print('****** reverse *****')
items = ['bangalore',2.2, 'pam', 3.3, 'andy', .3, 'eva', 1.2, 'allen', 'sam']
items.reverse()

print items



print('****** sort *****')
items = ['bangalore',2.2, 'pam', 3.3, 'andy', .3, 'eva', 1.2, 'allen', 'sam']
items.sort()
print items

items.sort(reverse=True) # kwargs reverse sort

print items










