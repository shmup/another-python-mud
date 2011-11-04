'''
Created on 2011-08-13

@author: Nich
'''
from queue import Queue
import threading
class CommandHandler(threading.Thread):
    '''
    Takes tokenized inputs from users, and matches them with a command
    '''
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.commandQueue = Queue()
    
    def addCommand(self, command):
        self.commandQueue.put(command)
    
    def process(self):
        if self.commandQueue.not_empty:
            comm = self.commandQueue.get()
            #Command lookup
            print(comm)
    def run(self):
        while 1:
            print(self.commandQueue)
            self.process()
                    