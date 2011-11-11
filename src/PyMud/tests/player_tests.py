'''
Created on Nov 10, 2011

@author: Nich
'''
import unittest
import player.player as p

class PlayerFactoryTest(unittest.TestCase):
    def setUp(self):
        self.player_store = {}
        self.fact = p.PlayerFactory(self.player_store)


    def tearDown(self):
        pass


    def testMakeNewPlayer(self):
        player1 = self.fact.newBuildPlayer("p1", "12345")
        self.assertEqual(player1, self.fact.getPlayer("p1", "12345"))
    
    def testCantGetWithBadPassword(self):
        _player1 = self.fact.newBuildPlayer("p1", "12345")
        self.assertEqual(None, self.fact.getPlayer("p1", "1234"))
        
    def testCantOverwriteExitingPlayer(self):
        player1 = self.fact.newBuildPlayer("p1", "12345")
        usurper = self.fact.newBuildPlayer("p1", "123456")
        self.assertEqual(None, usurper)
        self.assertEqual(player1, self.fact.getPlayer("p1", "12345"))
        self.assertEqual(self.fact.getPlayer("p1", "12345").password, "12345")
    
    
        
        
class PlayerTests(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testName(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()