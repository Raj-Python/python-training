from ps_account import  Account, Person


class SBAccount(Account):
    def __init__(self, acc_no, p, balance):
        self.balance = balance

        # invoking overrien methods
        super(SBAccount, self).__init__(acc_no, p)

    def get_info(self):
        super(SBAccount, self).get_info()
        print 'current balance :', self.balance

if __name__ == '__main__':
    sb = SBAccount('v5005', Person('jimmy', 'anderson'), 50.00)
    sb.get_info()


