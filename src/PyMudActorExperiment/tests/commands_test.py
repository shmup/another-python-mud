'''
Created on Nov 20, 2011

@author: Nich
'''

import unittest
from messanging.mail_sorter import MailSorter
from queue import Queue
import commands.commands as comm

class MailRecipient(object):
    def __init__(self, m_queue):
        self.message_queue = m_queue
        self.name = "Bob"
        
    def send(self, message):
        self.message_queue.put(message, False)



class CommandTest(unittest.TestCase):

    def setUp(self):
        self.mailQueue = Queue()
        self.mailsorter = MailSorter(self.mailQueue)
        
        
        self.s1 = MailRecipient(Queue())
        self.r1 = MailRecipient(Queue())
        self.r2 = MailRecipient(Queue())
        self.r3 = MailRecipient(Queue())

    def tearDown(self):
        pass


    def testSay(self):
        say = comm.say(self.r1)
        m1 = {"sender":self.s1, "targets":[self.r1, self.r2, self.r3], "args":"Hello folks"}
        say.send(m1)
        
        self.assertEqual(self.r1.message_queue.get(False), {"sender":self.s1, "recipients":[self.s1], "message": "You say, 'Hello folks'"})
        self.assertEqual(self.r1.message_queue.get(False), {"sender":self.s1, "recipients":[self.r1, self.r2, self.r3], "message":"Bob says, 'Hello folks'"})
    def testSayIntegration(self):
        say = comm.say(self.mailsorter.inbox())
        m1 = {"sender":self.s1, "targets":[self.r1, self.r2, self.r3], "args":"Hello folks"}
        say.send(m1)
        self.mailsorter.inbox().send(None)
        self.mailsorter.run()
        
        self.assertEqual(self.s1.message_queue.get(False)["message"], "You say, 'Hello folks'")
        self.assertEqual(self.r1.message_queue.get(False)["message"], "Bob says, 'Hello folks'")
        self.assertEqual(self.r2.message_queue.get(False)["message"], "Bob says, 'Hello folks'")
        self.assertEqual(self.r3.message_queue.get(False)["message"], "Bob says, 'Hello folks'")
        
    def testMult(self):
        mult = comm.mult(self.r1)
        m1 = {"sender":self.s1, "args":100}
        mult.send(m1)
        
        r_m1 = self.r1.message_queue.get(False)
        self.assertEqual(r_m1["message"], 100)
        self.assertEqual(r_m1["forwards"], [self.s1])
        
    def testMultIntegration(self):
        pass
        inbox = self.mailsorter.inbox()
        mult = comm.mult(inbox)
        m1 = {"sender":self.s1, "args":100}
        mult.send(m1)
        #This is a little tricky. We have to interrupt the mail handler in between each step by passing None as a sentinel
        inbox.send(None)
        self.mailsorter.run()
        inbox.send(None)
        self.mailsorter.run()
        self.assertEqual(self.s1.message_queue.get(False)["message"], 10000)
        
    
    def testHeavyCall(self):
        heavy = comm.heavy_call(self.r1)
        m1 = {"sender":self.s1, "message": 100, "forwards":[self.s1]}
        heavy.send(m1)
        self.assertEqual(self.r1.message_queue.get(False)["message"], 10000)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()