# raw string

file_path = r'c:\templates\neon\balances\rights\temp.txt'  # raw strings are prefixed as r
print file_path


#doc string ,for multiline formatted string

s = '''
            1
        2       2
    3       {}       3
        4       4
            5
'''

print s.format('x')