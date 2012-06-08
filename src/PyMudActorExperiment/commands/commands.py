'''
Created on Nov 19, 2011

@author: Nich
'''
from utils.coroutine import coroutine
import commands.async_commands

@coroutine
def say(inbox):
    while True:
        v_args = yield
        sender = v_args["sender"]
        local_area_targets = v_args["targets"]
        message = v_args["args"]
        inbox.send({"sender":sender, 
                    "recipients":[sender], 
                    "message":"You say, '"+message+"'"})
        
        inbox.send({"sender":sender, 
                    "recipients":local_area_targets, 
                    "message":sender.name+" says, '"+message+"'"})

#represents a heavyweight call
@coroutine
def heavy_call(inbox):
    while True:
        args = (yield)
        sender = args["sender"]
        recipients = args["forwards"]
        message = args["message"]
        import time
        time.sleep(int(message/1000))
        message = message*message
        inbox.send({"sender":sender, 
                    "recipients":recipients, 
                    "message":message})
        
#relies on a heavy call to get an answer back
@coroutine
def mult(inbox):
    while(True):
        args = (yield)
        sender = args["sender"]
        message = int(args["args"])
        inbox.send({"sender":sender,
                    "recipients":[heavy_call(inbox)], 
                    "message":message, 
                    "forwards": [sender]})
        
