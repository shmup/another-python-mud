'''
Created on Nov 19, 2011

@author: Nich
'''
import unittest
import mail_sorter as test
from queue import Queue
from multiprocessing import Queue as AQueue
import time

class MailRecipient(object):
    def __init__(self, m_queue):
        self.message_queue = m_queue
        
    def send(self, message):
        self.message_queue.put(message)





class MailSorterTest(unittest.TestCase):

    def setUp(self):
        self.mail_queue = Queue()
        self.r1 = MailRecipient(Queue())
        self.r2 = MailRecipient(Queue())
        self.r3 = MailRecipient(Queue())
        self.m1 = {"sender":("Bob"), "recipients":[self.r1, self.r2, self.r3], "message":"First message 3 recip"}
        self.m2 = {"sender":("Bob"), "recipients":[self.r3, self.r2], "message":"Second message 2 recip"}
        self.m3 = {"sender":("Bob"), "recipients":[self.r2], "message":"Third message 1 recip"}
        self.m4 = {"sender":("Bob"), "recipients":[], "message":"Fourth message no recip"}
        self.m5 = {"sender":("Bob"), "recipients":[self.r3, self.r2, self.r1], "message":"Fifth message recipients in different order"}
        self.m6 = {"sender":("Bob"), "recipients":[self.r3, self.r3], "message": "6th message, duplicate recipient"}
        
        
    def tearDown(self):
        pass

    def testSendToOne(self):
        self.mail_queue.put(self.m3, False)
        self.mail_queue.put(None, False)
        sorter = test.MailSorter(self.mail_queue)
        sorter.run()
        self.assertEqual(self.r2.message_queue.get(False), self.m3)
    
    def testSendToTwo(self):
        self.mail_queue.put(self.m2, False)
        self.mail_queue.put(None, False)
        sorter = test.MailSorter(self.mail_queue)
        sorter.run()
        self.assertEqual(self.r2.message_queue.get(False), self.m2)
        self.assertEqual(self.r3.message_queue.get(False), self.m2)
    
    def testSendToThree(self):
        self.mail_queue.put(self.m1, False)
        self.mail_queue.put(None, False)
        sorter = test.MailSorter(self.mail_queue)
        sorter.run()
        self.assertEqual(self.r1.message_queue.get(False), self.m1)
        self.assertEqual(self.r2.message_queue.get(False), self.m1)
        self.assertEqual(self.r3.message_queue.get(False), self.m1)
        
    def testRecvFunction(self):
        sorter = test.MailSorter(self.mail_queue)
        sorter.inbox().send(self.m1)
        sorter.inbox().send(self.m2)
        sorter.inbox().send(None)
        sorter.run()
        self.assertEqual(self.r1.message_queue.get(False), self.m1)
        self.assertEqual(self.r2.message_queue.get(False), self.m1)
        self.assertEqual(self.r3.message_queue.get(False), self.m1)
        self.assertEqual(self.r2.message_queue.get(False), self.m2)
        self.assertEqual(self.r3.message_queue.get(False), self.m2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()