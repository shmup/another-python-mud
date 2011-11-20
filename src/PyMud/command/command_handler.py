'''
Created on 2011-08-13

@author: Nich
'''
from multiprocessing import Process
import command_factory as fact
import multiprocessing
logger = multiprocessing.get_logger()

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
            logger.warning("processing command: %s", str(command))
            command.command["function"](command.context)

    def run(self):
        self.active = True
        while self.active:
            self.process_command()

        
            
                
'''
Need to find some way to integrate this with ordinary handlers
... needs to almost be a callback or yield system, since we're dealing asynchronously with command handler
Normal execution: User runs a command, Gets 0+ lines back, 0+ other users also get lines back
Normal execution: User inputs a bytestream, which is converted to a string by the handler and passed to the command handler. 
The command handler processes the command and puts it on a queue for execution. When the command executes, 
it sends the relevant messages to the relevant people
Normal execution: This class only worries about putting things on the queue, not getting anything back.

String command handler needs comm_queue, so that we can put commands into the queue, but we can't initialize it with it 
since that would break the CommandHandler interface. Not all the handlers need...
Why not add a variable arg, we can totally do that.

But then how do we know which args to pass? That won't work
Can grab the queue inside, but that's opaque, difficult to test, and bad practice
Can pass the queue into the message. Probably a good option, but breaks the interface (handle_data doesn't take a queue)

Could delegate queue methods to a different class initialized before...
Ugh, is that really the best option? A Queue proxy? Is this what we've come to?

No, we'd probably just end up trying to grab the queue proxy which is just as bad
'''
class StringCommandHandler(object):
    def __init__(self, comm_queue):
        self.comm_queue = comm_queue
    def put(self, caller_command):
        print("String command handler called")
        self.comm_queue.put(fact.command_factory(caller_command))
