'''
Created on Nov 10, 2011

@author: Nich
'''
import unittest
import command.command_utils as test

class Test(unittest.TestCase):
    def setUp(self):
        self.commands = {"say":"say",
                         "say to": "say to",
                         "say to me": "say to me",
                        }

    def testMerge(self):
        text = ["alpha", "beta", "gamma"]
        self.assertEquals(test.merge_text(text, 0), "alpha")
        self.assertEquals(test.merge_text(text, 1), "alpha beta")
        self.assertEquals(test.merge_text(text, 2), "alpha beta gamma")
        
    def testSplit(self):
        text = "alpha beta gamma"
        self.assertEqual(test.split_command(text), ["alpha", "beta", "gamma"])
        
    def testMatch(self):
        
        self.assertEqual(test.match_command(["say"], self.commands), ("say", ""))
        self.assertEqual(test.match_command(["say", "to"], self.commands), ("say to", ""))
        self.assertEqual(test.match_command(["say","to","me"], self.commands), ("say to me", ""))
    
    def testMatchArgs(self):
        comm = {
                  "say":"say",
                  "say to": "say to",
                  "say to me":"say to me",
                  }
        self.assertEqual(test.match_command(["say", "of", "you"], comm), ("say", "of you"))
        self.assertEqual(test.match_command(["say", "to", "you"], comm), ("say to", "you"))
        self.assertEqual(test.match_command(["say","to","me"], comm), ("say to me", ""))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMerge']
    unittest.main()