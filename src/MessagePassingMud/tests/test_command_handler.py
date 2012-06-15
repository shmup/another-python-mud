'''
Created on Jun 4, 2012

@author: Nich
'''
import unittest
from command_handler import command_handler
#from mocks.mock_player import Player
from player.player import get_default
from tests.mocks.mock_connection import Connection
from tests.mocks.mock_command_matcher import match_command


class TestCommandHandler(unittest.TestCase):


    def setUp(self):
        p = get_default()
        self.c = Connection()
        cm = match_command
        self.ch = command_handler(p, self.c, cm)


    def tearDown(self):
        pass


    def testSimpleCommand(self):
        self.ch.send("say Hello World")
        self.assertEqual(self.c.msgs, [("info", "executing say with arguments Hello World")])
        
    def testMultipleCommands(self):
        self.ch.send("say Hello World")
        self.ch.send("up")
        self.ch.send("move 2 n")
        self.assertEqual(self.c.msgs, [("info", "executing say with arguments Hello World"),  ("info", "executing up with arguments "),  ("info", "executing move with arguments 2 n")])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()