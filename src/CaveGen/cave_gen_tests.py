'''
Created on Nov 16, 2011

@author: Nich
'''
import unittest
import cave_gen

class Test(unittest.TestCase):


    def setUp(self):
        self.seed = 1337
        


    def tearDown(self):
        pass

    def testTransitivity(self):
        self.assertEqual(cave_gen.generate((0, 0, 0), (10, 10, 10), cave_gen.generate_value), cave_gen.generate((10, 10, 10), (0, 0, 0), cave_gen.generate_value))

    def testDimensionality(self):
        test1 = [[[1, 1, 1],[1, 1, 1],[1, 1, 1]],[[1, 1, 1],[1, 1, 1],[1, 1, 1]],[[1, 1, 1],[1, 1, 1],[1, 1, 1]]]
        test2 = [[[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]],[[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]],[[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]]
        test3 = [[[1, 1],[1, 1],[1, 1]],[[1, 1],[1, 1],[1, 1]],[[1, 1],[1, 1],[1, 1]], [[1, 1],[1, 1],[1, 1]]]
        self.assertEquals([3, 3, 3], cave_gen.calculate_dimensionality(test1, []))
        self.assertEquals([3, 3, 4], cave_gen.calculate_dimensionality(test2, []))
        self.assertEquals([4, 3, 2], cave_gen.calculate_dimensionality(test3, []))
    def testOrderOfGeneratedMap(self):
        cave1 = cave_gen.generate((0, 0, 0), (10, 10, 10), cave_gen.generate_value)
        self.assertEqual(3, cave_gen.calculate_order(cave1, []))
        
                            
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()