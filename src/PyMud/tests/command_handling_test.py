'''
Created on Nov 9, 2011

@author: Nich
'''

#Todo: get mock framework, so we can make sure that the commands actually execute

import unittest
import command.command_handler #@UnresolvedImport
import time

def some_func(x):
    print(x["args"])

class CommandProcessingTest(unittest.TestCase):


    def setUp(self):
        self.handler = command.command_handler.CommandHandler()
        #self.handler.start()

    def tearDown(self):
        pass


    def testCommandsEnterAndExit(self):
        self.assertTrue(self.handler.empty(), "Queue not empty at start")
        c1 = command.command_handler.Command({"function":some_func, "requires":["args"]}, {"args":"some args"})
        self.handler.put(c1)
        time.sleep(0.1)
        self.assertFalse(self.handler.empty() , "Queue empty after inserting one command")
        self.handler.run()
        self.assertTrue(self.handler.empty(), "Queue not empty after processing one command")
        
        
    def testAddRemoveTwo(self):
        c1 = command.command_handler.Command({"function":some_func, "requires":["args"]}, {"args":"some args1"})
        c2 = command.command_handler.Command({"function":some_func, "requires":["args"]}, {"args":"some args2"})
        self.assertTrue(self.handler.empty(), "Queue is not empty at start")
        self.handler.put(c1)
        self.handler.put(c2)
        time.sleep(0.1)
        self.assertFalse(self.handler.empty(), "Queue is empty after inserting two")
        self.handler.run()
        self.handler.run()
        self.assertTrue(self.handler.empty(), "Queue is not empty after running twice")
        
    def testAddRemoveInterleave(self):
        self.assertTrue(self.handler.empty(), "Queue not empty at start")
        c1 = command.command_handler.Command({"function":some_func, "requires":["args"]}, {"args":"some args"})
        self.handler.put(c1)
        time.sleep(0.1)
        self.assertFalse(self.handler.empty() , "Queue empty after inserting one command first time")
        self.handler.run()
        self.assertTrue(self.handler.empty(), "Queue not empty after processing one command first time")
        self.handler.put(c1)
        time.sleep(0.1)
        self.assertFalse(self.handler.empty() , "Queue empty after inserting one command second time")
        self.handler.run()
        self.assertTrue(self.handler.empty(), "Queue not empty after processing one command second time")    
    
    def testRunEmptyQueueDoesNothing(self):
        self.handler.run()
      


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()