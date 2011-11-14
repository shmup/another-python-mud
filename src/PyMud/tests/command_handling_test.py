'''
Created on Nov 9, 2011

@author: Nich
'''

#Todo: get mock framework, so we can make sure that the commands actually execute

import unittest
import command.command_handler #@UnresolvedImport
from command.command_factory import Command
import queue #@UnresolvedImport

def some_func(x):
    print(x["args"])

class CommandProcessingTest(unittest.TestCase):


    def setUp(self):
        self.comm_queue = queue.Queue()
        self.handler = command.command_handler.CommandProcess(self.comm_queue)
        

    def tearDown(self):
        pass


    def testCommandsEnterAndExit(self):
        self.assertTrue(self.handler.empty(), "Queue not empty at start")
        c1 = Command({"function":some_func, "requires":["args"]}, {"args":"some args"})
        self.comm_queue.put(c1)
        self.assertFalse(self.handler.empty() , "Queue empty after inserting one command")
        self.handler.process_command()
        self.assertTrue(self.handler.empty(), "Queue not empty after processing one command")
        
        
    def testAddRemoveTwo(self):
        c1 = Command({"function":some_func, "requires":["args"]}, {"args":"some args1"})
        c2 = Command({"function":some_func, "requires":["args"]}, {"args":"some args2"})
        self.assertTrue(self.handler.empty(), "Queue is not empty at start")
        self.comm_queue.put(c1)
        self.comm_queue.put(c2)
        self.assertFalse(self.handler.empty(), "Queue is empty after inserting two")
        self.handler.process_command()
        self.handler.process_command()
        self.assertTrue(self.handler.empty(), "Queue is not empty after running twice")
        
    def testAddRemoveInterleave(self):
        self.assertTrue(self.handler.empty(), "Queue not empty at start")
        c1 = Command({"function":some_func, "requires":["args"]}, {"args":"some args"})
        self.comm_queue.put(c1)
        self.assertFalse(self.handler.empty() , "Queue empty after inserting one command first time")
        self.handler.process_command()
        self.assertTrue(self.handler.empty(), "Queue not empty after processing one command first time")
        self.comm_queue.put(c1)
        self.assertFalse(self.handler.empty() , "Queue empty after inserting one command second time")
        self.handler.process_command()
        self.assertTrue(self.handler.empty(), "Queue not empty after processing one command second time")    
    
    def testRunEmptyQueueDoesNothing(self):
        self.handler.process_command()
      


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()