'''
Created on Nov 15, 2011

@author: Nich
'''
import unittest
import network.mudserver #@UnresolvedImport


class A():
    def __init__(self, next_handler, conn=None):
        self.next = next_handler
class B():
    def __init__(self, next_handler, conn=None):
        self.next = next_handler
class C():
    def __init__(self, next_handler, conn=None):
        self.next = next_handler

class CommandHandlerStackTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def testEmptyStack(self):
        command_stack = []
        commands = network.mudserver.create_chain(command_stack, None)
        self.assertEqual(commands, None)
        
    def testBuildStack(self):
        command_stack = [A]
        commands = network.mudserver.create_chain(command_stack, None)
        self.assertTrue(isinstance(commands, A))
    
    def testBuild2Stack(self):
        command_stack = [A, B]
        commands = network.mudserver.create_chain(command_stack, None)
        self.assertTrue(isinstance(commands, A))
        self.assertTrue(isinstance(commands.next, B))
    
    def testBuild3Stack(self):
        command_stack = [A, B, C]
        commands = network.mudserver.create_chain(command_stack, None)
        self.assertTrue(isinstance(commands, A))
        self.assertTrue(isinstance(commands.next, B))
        self.assertTrue(isinstance(commands.next.next, C))
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()