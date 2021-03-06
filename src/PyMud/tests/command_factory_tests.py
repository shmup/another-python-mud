'''
Created on Nov 10, 2011

@author: Nich
'''
import unittest
import command.command_factory as test

DEFAULT_FUNC = 123
CALLER = 1234

class Test(unittest.TestCase):


    def setUp(self):
        self.commands = {
                         "say": {
                                 "function": "say",
                                 "requires":["args"]
                                 },
                         "say to":{
                                   "function": "say to",
                                   "requires":["args"]
                                   },
                         "say to me":{
                                   "function": "say to me",
                                   "requires":["args", "targets_in_area"]
                                   },
                         "default":{
                                    "function": DEFAULT_FUNC,
                                    "requires": "sender"
                                    }
                         }
        self.command1 = test.command_factory((CALLER, "say to Jim I'm sleepy"), self.commands)
        self.command2 = test.command_factory((CALLER, "say I'm sleepy"), self.commands)
        self.command3 = test.command_factory((CALLER, "say to me I'm sleepy"), self.commands)

    def tearDown(self):
        pass


    def testCorrectFunctionsGetPassed(self):
        self.assertEqual(self.command1[0]["function"], "say to")
        self.assertEqual(self.command2[0]["function"], "say")
        self.assertEqual(self.command3[0]["function"], "say to me")
        
    def testCorrectArgsGetPassed(self):
        self.assertEqual(self.command1[1]["args"], "Jim I'm sleepy")
        self.assertEqual(self.command2[1]["args"], "I'm sleepy")
        self.assertEqual(self.command3[1]["args"], "I'm sleepy")
    
    def testFunctionNotFoundReturnsDefault(self):
        default = test.command_factory("asdfas", self.commands)    
        self.assertEqual(default[0]["function"], DEFAULT_FUNC)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
