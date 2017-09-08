import unittest


# setup for Module level
def setUpModule():
    print "fix for the module"

# tearDown for Module level
def tearDownModule():
    print "fix for the module"



class FixtureTest(unittest.TestCase):


    # setup for class level
    @classmethod
    def setUpClass(cls):
        print 'in setUpClass()'
        cls.fixture = range(1, 10)

    # Teardown  for class level
    @classmethod
    def tearDownClass(cls):
        print 'in tearDownClass()'
        del cls.fixture

    # runs for every test method
    def setUp(self):
        print 'in setup()'
        self.fixture = range(1, 10)

    # runs for every test method
    def tearDown(self):
        print 'In teardown()'
        del self.fixture


    def test_alpha(self):
        print 'In test()'
        self.failUnlessEqual(self.fixture, range(1, 10))

    def test_beta(self):
        print 'In test()'
        self.assertIn(self.fixture[3], range(1, 10))


if __name__ == '__main__' :
    unittest.main()



