'''
Created on Nov 10, 2011

@author: Nich
'''
import unittest
import network.connection as test

class TestConnectionHandler(object):
    def __init__(self):
        self.addr = 0
        self.sock = 0
    
    def send(self, message):
        print(message)

class TestCommandHandler(object):
    pass
class TestPlayerFactory(object):
    pass    
    
class ConnectionTest(unittest.TestCase):
    def setUp(self):
        handler = TestConnectionHandler()
        command_handler = TestCommandHandler()
        playerfact = TestPlayerFactory()
        self.conn = test.Connection(0, handler, command_handler, playerfact)
    def tearDown(self):
        pass
    def testSend(self):
        #just make sure this doesn't fail
        self.conn.send("Hello")

class ConnectionFactoryTest(unittest.TestCase):

    def setUp(self):
        self.conn_store = {}
        comm_handler = TestCommandHandler()
        playerfact = TestPlayerFactory()
        self.connection_handler = TestConnectionHandler()
        self.fact = test.ConnectionFactory(self.conn_store, comm_handler, playerfact)


    def tearDown(self):
        pass


    def testRegisterOne(self):
        con1 = self.fact.register_connection(self.connection_handler)
        self.assertEqual(con1, self.fact.get_by_id(con1.c_id))
        
    def testAddDelete(self):
        con1 = self.fact.register_connection(self.connection_handler)
        self.fact.deregister_connection(con1.c_id)
        self.assertIsNone(self.fact.get_by_id(con1.c_id))
        
    def testAddDeleteDoesntAffectOther(self):
        con1 = self.fact.register_connection(self.connection_handler)
        con2 = self.fact.register_connection(self.connection_handler)
        self.fact.deregister_connection(con1.c_id)
        self.assertIsNone(self.fact.get_by_id(con1.c_id))
        self.assertEqual(con2, self.fact.get_by_id(con2.c_id))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()