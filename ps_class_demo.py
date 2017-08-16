# Class Names should be of camel case
# not mandatory to create constructor or destructor
# new rule is the class should be passed with object class
# private members shoud start with __
# access private members from public methods

import math
import os
import sys


class Demo(object):

    def __init__(self):
        print self, 'am in constructor'

    def __del__(self):
        print self, 'getting destroyed'


d = Demo()
print d
print Demo
print __name__ # to get default name space of a script
print os.__name__
print math.__name__
print sys.__name__