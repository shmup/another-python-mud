'''
Created on 2011-08-13

@author: Nich
'''
from multiprocessing import Process
import collections
import command_factory as fact

#Todo: Add option to supply queue to avoid timing issues in testing

class CommandProcess(Process):
    
    def __init__(self, commandQueue):
        Process.__init__(self)
        self.commandQueue = commandQueue
        self.active = False
        
    def put(self, command):
        self.commandQueue.put(command, True, None)
    
    def empty(self):
        return self.commandQueue.empty()
    
    

    def process_command(self):
        if not self.commandQueue.empty():
            command = self.commandQueue.get(True, None)
            command.command["function"](command.context)

    def run(self):
        self.active = True
        while self.active:
            self.process_command()

        
            
                

class StringCommandHandler(object):
    def __init__(self, comm_queue):
        self.comm_queue = comm_queue
    def put(self, command_text):
        self.comm_queue.put(fact.command_factory(command_text))
        

Command = collections.namedtuple("Command", ["command", "context"])              