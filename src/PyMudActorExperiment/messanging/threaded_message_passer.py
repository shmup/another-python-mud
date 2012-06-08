'''
Created on Nov 22, 2011

@author: Nich
'''
import threading
from coroutine import coroutine
from queue import Queue


class Messanging(object):
    def __init__(self, func):
        self.func = func
        self.message_queue = Queue()
        
    def pass_m(self, m):
        self.message_queue.put(m)
    
    def run(self):
        while True:
            m = self.message_queue.get()
            if m == None:
                break
            self.func.send(m)
    
    def __call__(self, *args, **kwargs):
        f = self.func(*args, **kwargs)
        f.__setattr__("pass_m", self.pass_m)
        f.__setattr__("run", self.runs)
        
        return f

@Messanging
@coroutine
def print_stuff():
    while(True):
        m = yield
        print(m)
    
    



if __name__ == '__main__':
    m = print_stuff()
    print(dir(m))
    m.send("Hello World 1")
    m.send("Hello World 2")
    m.send("Hello World 3")
    m.send(None)
    
    #m.run()
    