'''
Created on Jun 4, 2012

@author: Nich
'''
import unittest
from MessagePassingMud.map.directions import dirs, add_dirs

class TestAddDirections(unittest.TestCase):


    def testAdd111(self):
        res = add_dirs((0, 0, 0), (1, 1, 1))
        self.assertEqual(res, (1, 1, 1))

    def testAddNorth(self):
        res = add_dirs(dirs["n"], (0, 0, 0))
        self.assertEqual(res, (0, 1, 0))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()