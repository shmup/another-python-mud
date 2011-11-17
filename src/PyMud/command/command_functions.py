'''
Created on Nov 9, 2011

@author: Nich
'''
import sys
def say(context):
    command = {"sender":context["sender"], "command":"say", "args":context["args"]}
    context["sender"].handle_command(command)
    for person in context["local_area_targets"]:
        person.handle_command(command)
    
def default(context):
    print("blah blah blah")
    context["sender"].send("I don't understand that")
    
def com_close(context):
    sys.exit("Oops")