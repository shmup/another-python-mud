'''
Created on Jun 29, 2012

@author: Nich
'''
import unittest
from commands import *
from tests.mocks.mock_player import Player


class Test(unittest.TestCase):
    def setUp(self):
        self.p = Player()

    def testDig(self):
        msg = dig(self.p, "e")
        self.assertEqual(msg[0][0], "info")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()