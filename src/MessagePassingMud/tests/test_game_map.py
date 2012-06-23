'''
Created on Jun 18, 2012

@author: Nich
'''
import unittest
from map.game_map import GameMap
from tests.mocks.mock_data_map import DataMap
from tests.mocks.mock_map_gen import gen_tile


class Test(unittest.TestCase):


    def setUp(self):
        self.game_map = GameMap(gen_tile, DataMap)


    def tearDown(self):
        pass


    def testDig(self):
        locs = [(0, 0), (0, 0), (0, 3), (3, 5), (5, 7), (7, 5), (5, 3), (3, 0)]
        nlocs = [(0, 1), (0, 5), (2, 3), (3, 6), (5, 70), (8, 5), (5, -3), (3, 20)]
        for loc in locs:
            self.game_map.dig(loc)
        
        for loc in locs:
            self.assertEqual(self.game_map.map_cache[loc], 0, "testing "+str(loc))
        
        for nloc in nlocs:
            self.assertEqual(self.game_map.get(nloc), 1, "testing "+str(nloc))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()