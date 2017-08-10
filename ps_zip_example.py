from pprint import pprint as pp

names = ['joe', 'pat', 'kim', 'tim']
gender = ['male', 'male', 'female', 'male']
age = ['2', '3', '1', '5']


pp(zip(names, gender, age))
print
print


# parallel iteration

for n, g, a in zip(names, gender, age):
    print "{:>22} {:>22} {:>10}".format(n, g, a)

print"-----------------------------------------"


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]


mat[1][1] = 'x'
mat[2].append(10)

for row in mat:
    for col in row:
        print col, '\t',
    print

