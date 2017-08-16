class PackageManager(object):
    def __init__(self, name, version):
        self.__name = name
        self.version = version

    def __get_information2(self):
        print 'name :' , self.__name
        print 'version :', self.version


    def get_information(self):
        print 'name :' , self.__name
        print 'version :', self.version


    def wrapper(self):
        self.__get_information2()


pm = PackageManager('pip', '2.2.18')
pm.get_information()
print pm.version

pm.wrapper()