'''
Created on Jun 28, 2012

@author: Nich
'''
import unittest
from tests.mocks.mock_game_map import GameMap
from tests.mocks.mock_data_map import DataMap
from player.player import Player

class Test(unittest.TestCase):


    def setUp(self):
        self.gmap = GameMap(db = DataMap(), input_map = {(-1, -1):1, (-1, 0):1, (-1, 1): 1,
                (0, -1): 2, (0, 0): 0, (0, 1): 0,
                (1, -1): 1, (1, 0): 0, (1, 1): 1})
        self.player = Player(local_map = self.gmap)


    def tearDown(self):
        pass


    def testSetLocationIfOpen(self):
        loc = (1, 0)
        res = self.player.set_location(loc)
        self.assertEqual(self.player.location, loc)
        self.assertTrue(res)
        
    def testSetLocationIfClosed(self):
        loc = (-1, 0)
        res = self.player.set_location(loc)
        self.assertEqual(self.player.location, (0, 0))
        self.assertFalse(res)
        
    def testMoveSuccess(self):
        dir = "e"
        self.player.move(1, dir)
        self.assertEqual(self.player.location, (1, 0))
        
    def testMoveFail(self):
        dir = "w"
        self.player.move(1, dir)
        self.assertEqual(self.player.location, (0, 0))
        
    def testDigSuccess(self):
        dir = "d"
        self.player.dig(1, dir)
        self.assertEqual(self.player.location, (0, -1))
        self.assertEqual(self.gmap.get((0, -1)), 0)
    
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()