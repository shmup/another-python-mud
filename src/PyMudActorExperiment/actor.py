'''
Created on Nov 27, 2011

@author: Nich
'''
import threading
import queue
from MessagePassingMud.utils import coroutine


class Actor(object):
    def __init__(self):
        self.out_thread = threading.Thread(target = self.out)
        self.processing_thread = threading.Thread(target = self.run)
        self.in_queue = queue.Queue()
        self.out_queue = queue.Queue()
        
    def run(self):
        while(True):
            m = self.in_queue.get()
            if m == None:
                break
            result = self.process(m)
            self.out_queue.put(result)
    
    def out(self):
        while(True):
            m = self.out_queue.get()
            if m == None:
                break
            if not m.recipients is None: 
                for r in m.recipients:   
                    r.send(m)
            
    def process(self, message):
        pass
    
    @coroutine
    def inbox(self):
        while True :
            m = yield
            self.in_queue.put(m)
        
    def start(self):
        self.processing_thread.start()
        self.out_thread.start()
        
    def close(self):
        self.out_thread.close()
        self.processing_thread.close()