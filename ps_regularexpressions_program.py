## given a pattern search in all files given and print the filename , line number and line


import re

print '\n\n'
print '1 --------------  crude way of coding  ---------------------'
def search_regex(pattern, file1, file2):

    with open(file1) as fr:
        line_num = 0 ;
        for line in fr:
            line_num += 1
            for m in re.finditer(pattern, line, re.I):
                print '{} -> {} -> {}'.format(file1, line_num, line)

    with open(file2) as fr:
        line_num = 0 ;
        for line in fr:
            line_num += 1
            for m in re.finditer(pattern, line, re.I):
                print '{} -> {} -> {}'.format(file2, line_num, line)



search_regex('bash', 'resources/passwd.txt', 'resources/data1.txt')




print '\n\n'
print '1 --------------  better way , the pythonic way ---------------------'
from fileinput import input, filelineno, filename

def grep_me(pattern, file_names):
    for line in input(file_names):
        if re.search(pattern, line, re.I):
            print "{}:{}:{}".format(filename(), filelineno(), line),




grep_me('bash$', ['resources/passwd.txt', 'resources/data1.txt'])