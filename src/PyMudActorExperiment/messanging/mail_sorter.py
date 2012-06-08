'''
Created on Nov 19, 2011

Receives messages, and routes them to their destination

@author: Nich
'''
from utils.coroutine import coroutine


#TODO: Make this run in its own process. See if that fixes the long process issue. The long process should be in its own process as well, but...

class MailSorter(object):
    '''
    classdocs
    '''

    def __init__(self, mail_queue):
        self.mail_queue = mail_queue
    
    @coroutine
    def inbox(self):
        while True:
            m = (yield)
            self.mail_queue.put(m)
        
    def run(self):
        while True:
            m = self.mail_queue.get()
            if m == None:
                break
            recip = m["recipients"]
            for r in recip:
                r.send(m)
            
        