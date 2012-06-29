'''
Created on Jun 23, 2012

@author: Nich
'''
import unittest
from tests.mocks.mock_game_map import GameMap
import map.map_display_functions as map_gens



class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGenerateMakesCorrectSize(self):
        gmap = GameMap()
        pos = (0, 0)
        size = (20, 20)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertEqual(len(dmap.items()), size[0]*size[1])
        
        pos = (-5, -8)
        size = (20, 21)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertEqual(len(dmap.items()), size[0]*size[1])
        
        pos = (-5, 8)
        size = (21, 21)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertEqual(len(dmap.items()), size[0]*size[1])
        
        pos = (5, -8)
        size = (21, 20)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertEqual(len(dmap.items()), size[0]*size[1])
        
        pos = (5, -8)
        size = (1, 20)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertEqual(len(dmap.items()), size[0]*size[1])
        
    def testGenerateMakesCorrectRange(self):
        gmap = GameMap()
        pos = (10, 10)
        size = (21, 21)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertFalse((-1, -1) in dmap, "(-1, -1) is not in dmap")
        self.assertTrue((0, 0) in dmap, "(0, 0) is in dmap")
        self.assertFalse((0, 21) in dmap, "(0, 21) is not in dmap")
        self.assertTrue((0, 20) in dmap, "(0, 20) is in dmap")
        self.assertFalse((21, 0) in dmap, "(21, 0) is not in dmap")
        self.assertTrue((20, 0) in dmap, "(20, 0) is in dmap")
        self.assertFalse((21, 21) in dmap, "(21, 21) is not in dmap")
        self.assertTrue((20, 20) in dmap, "(20, 20) is in dmap")
        
        gmap = GameMap()
        pos = (11, 11)
        size = (10, 10)
        
        dmap = map_gens.generate(pos, size, gmap)
        self.assertFalse((5, 5) in dmap, "(5, 5) is not in dmap")
        self.assertTrue((6, 6) in dmap, "(6, 6) is in dmap")
        self.assertFalse((6, 16) in dmap, "(6, 17) is not in dmap")
        self.assertTrue((6, 15) in dmap, "(6, 16) is in dmap")
        self.assertFalse((16, 6) in dmap, "(17, 6) is not in dmap")
        self.assertTrue((15, 6) in dmap, "(16, 6) is in dmap")
        self.assertFalse((16, 16) in dmap, "(17, 17) is not in dmap")
        self.assertTrue((15, 15) in dmap, "(16, 16) is in dmap")
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()