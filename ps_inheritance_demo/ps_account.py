from  ps_inheritance_demo.ps_person import Person

class Account(object):
    def __init__(self, acc_no, p_ref):
        self.acc_no = acc_no
        self.person = p_ref


    def get_info(self):
        print 'account no: ', self.acc_no
        self.person.get_info()


if __name__ == '__main__':
    p = Person('guido', 'rossum')
    acc = Account('v4004', p)
    acc.get_info()