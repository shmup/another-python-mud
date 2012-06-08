'''
Created on Nov 21, 2011

@author: Nich
'''
from coroutine import coroutine



#Running in another process
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
        
#running in the main process
def heavy_call_proxy(inbox):
    while True:
        m = (yield)
        