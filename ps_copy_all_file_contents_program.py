# last file is target file where all other files contents are written to it.



def copy_all(*args):
    if len(args) < 2:
        raise TypeError("insuff .... args/")

    try:
        with open(args[-1], 'w') as fw:
            for file_name in args[:-1]:
                fw.write(file_name.center(60, '-') + "\n")
                fw.write(open(file_name).read())
                fw.write('-' * 60 + '\n')

    except IOError as err:
        print err


copy_all('resources/f1.txt','resources/f2.txt','resources/f3.txt')
copy_all('resources/f1.txt')
