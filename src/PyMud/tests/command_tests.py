'''
Created on Nov 10, 2011

@author: Nich
'''
import unittest
import command.command_functions as com

class TestPlayer(object):
    def __init__(self, name):
        self.name = name
        self.message = ''
        
    def handle_command(self, arg):
        self.message = arg

class TestObject(object):
    def __init__(self, name):
        self.name = name
        self.message = ''
        
    def handle_command(self, arg):
        self.message = arg

class Test(unittest.TestCase):


    def setUp(self):
        self.p1 = TestPlayer("p1")
        self.p2 = TestPlayer("p2")
        self.p3 = TestPlayer("p3")
        self.o1 = TestObject("o1")
        self.caller = self.p1
        self.targets = [self.p2, self.p3, self.o1]

    def tearDown(self):
        pass


    def testSay(self):
        context = {"sender":self.p1, "local_area_targets":self.targets, "args":"hello"}
        com.say(context)
        self.assertEqual(self.p1.message, {"sender":self.p1, "command":"say", "args":"hello"})
        self.assertEqual(self.p2.message, {"sender":self.p1, "command":"say", "args":"hello"})
        self.assertEqual(self.p3.message, {"sender":self.p1, "command":"say", "args":"hello"})
        self.assertEqual(self.o1.message, {"sender":self.p1, "command":"say", "args":"hello"})
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()