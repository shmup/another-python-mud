'''
Created on Nov 9, 2011

@author: Nich
'''
import sys
def say(message):
    sender = message["sender"]
    args = message["message"]["args"]
    command = {"sender":sender, "message":{"command":"say", "args":args}}
    sender.send(command)
    local_area_targets = message["message"]["local_area_targets"]
    for person in local_area_targets:
        person.send(command)
    
def default(context):
    print("blah blah blah")
    context["sender"].send("I don't understand that")
    
def com_close(context):
    sys.exit("Oops")