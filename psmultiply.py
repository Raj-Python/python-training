#num = int(raw_input('enter the input number'))


## incomplete program , please complete it


def prod(num):
    row = 1
    col = 1
    print '*',

    while(row <= num):
        print row ,
        while(col <= num):
            print row * col,
            col = col + 1
        row += 1








prod(10)