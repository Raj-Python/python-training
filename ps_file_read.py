# default the mode is read

with open('resources/passwd.txt') as fp:
    print fp
    for line in fp:
        print line,


print fp