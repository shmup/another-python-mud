'''
Created on Jun 18, 2012

@author: Nich
'''
import unittest
from map.game_map import GameMap, normalize, dig
from tests.mocks.mock_data_map import DataMap
from tests.mocks.mock_map_gen import gen_tile


class Test(unittest.TestCase):


    def setUp(self):
        self.game_map = GameMap(gen_tile, DataMap)


    def tearDown(self):
        pass


    def testDig(self):
        locs = [(0, 0), (0, 3), (3, 5), (5, 7), (7, 5), (5, 3), (3, 0)]
        nlocs = [(0, 1), (0, 5), (2, 3), (3, 6), (5, 70), (8, 5), (5, -3), (3, 20)]
        for loc in locs:
            dig(loc, self.game_map)
        
        for loc in locs:
            self.assertEqual(self.game_map.map_cache[loc], 0, "testing "+str(loc))
        
        for nloc in nlocs:
            self.assertEqual(self.game_map.get(nloc), 1, "testing "+str(nloc))
            
            
    def testSet(self): 
        loc = (423, 523)
        self.game_map.set(loc, 5)
        self.assertEqual(self.game_map.get(loc), 5, "Testing get after set")
        self.assertEqual(self.game_map.map_cache[loc], 5, "Testing that the value is in the cache")

        loc = (-423, -523)
        self.game_map.set(loc, 5)
        self.assertEqual(self.game_map.get(loc), 5, "Testing get after set")
        self.assertEqual(self.game_map.map_cache[loc], 5, "Testing that the value is in the cache")
        
        loc = (423, 523)
        self.game_map.set(loc, -5)
        self.assertEqual(self.game_map.get(loc), -5, "Testing get after set")
        self.assertEqual(self.game_map.map_cache[loc], -5, "Testing that the value is in the cache")

    
    def testGet(self):
        locs = [(0, 0), (0, 3), (3, 5), (5, 7), (7, 5), (5, 3), (3, 0)]
        nlocs = [(0, 1), (0, 5), (2, 3), (3, 6), (5, 70), (8, 5), (5, -3), (3, 20)]
        for loc in locs:
            self.game_map.set(loc, 0)
            
        for loc in locs:
            self.assertEqual(self.game_map.map_cache[loc], 0, "testing "+str(loc))
        
        for nloc in nlocs:
            self.assertEqual(self.game_map.get(nloc), 1, "testing "+str(nloc))
        
    def testCacheNext(self):
        loc = (0, 0)
        size = (50, 50)
        self.game_map.cache_next(loc, size)
        self.assertEqual(len(self.game_map.map_cache.items()), size[0]*size[1])
    
    def test_normalize(self):
        pos = (90, 90)
        gmap = {(100, 100):1, (80, 80):1, (74, 80):1}
        size = (33, 20)
        
        nmap = normalize(gmap, pos, size)
        
        self.assertEqual(nmap, {"26_20":1, "6_0":1, "0_0":1})
    
    def testMergeMap(self):
        
        pass
        
        
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()