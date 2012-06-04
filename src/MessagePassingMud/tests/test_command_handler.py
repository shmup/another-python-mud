'''
Created on Jun 4, 2012

@author: Nich
'''
import unittest
from MessagePassingMud.command.command_handler import command_handler
#from mocks.mock_player import Player
from MessagePassingMud.player.player import get_default
from MessagePassingMud.tests.mocks.mock_connection import Connection
from MessagePassingMud.tests.mocks.mock_command_matcher import match_command


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
        self.assertEqual(self.c.msgs, [b"executing say with arguments Hello World\n", b"Nicholas: say Hello World"])
        
    def testMultipleCommands(self):
        self.ch.send("say Hello World")
        self.ch.send("up")
        self.ch.send("move 2 n")
        self.assertEqual(self.c.msgs, [b"executing say with arguments Hello World\n", b"Nicholas: say Hello World",b"executing up with arguments \n", b"Nicholas: up", b"executing move with arguments 2 n\n", b"Nicholas: move 2 n"])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()