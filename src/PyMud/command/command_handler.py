'''
Created on 2011-08-13

@author: Nich
'''
from multiprocessing import Process, Queue
import time
import collections

#Todo: Add option to supply queue to avoid timing issues in testing

class CommandHandler(Process):
    
    def __init__(self):
        Process.__init__(self)
        self.commandQueue = Queue()
        
    def put(self, command):
        self.commandQueue.put(command, True, None)
    
    def empty(self):
        return self.commandQueue.empty()
    
    
    def run(self):
        if self.commandQueue.empty():
            pass
        else:
            command = self.commandQueue.get(True, None)
            command.command["function"](command.context)


Command = collections.namedtuple("Command", ["command", "context"])              