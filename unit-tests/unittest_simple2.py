import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        self.failUnless(True)

class OutcomesTest(unittest.TestCase):
    def testPass(self):
        return


    def testFail(self):
        self.failIf(False)


    def testError(self):
        #raise RuntimeError('Test error!')
        pass



    @unittest.skip('causes an error')   # to skip the test
    def testSkip(self):
        #raise RuntimeError('Test error!')
        pass








if __name__ == '__main__' :
    unittest.main()