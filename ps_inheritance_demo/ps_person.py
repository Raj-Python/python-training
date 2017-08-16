class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        print 'first name :', self.first_name
        print 'last name :' , self.last_name


if __name__ == '__main__':
    p = Person('larry', 'wall')
    p.get_info()
    print __name__


