class Alpha(object):
    def pprint(self):
        print 'pprint from the class alpha'


class Beta(Alpha):
    def pprint(self):
        print 'pprint from the call Alphaaaaa'


class Charlie(Beta):
    def pprint(self):
        super(Beta, self).pprint()



if __name__ == '__main__':
    Charlie().pprint()