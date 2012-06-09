'''
Created on May 22, 2012

@author: Nich
'''
from MessagePassingMud.utils.coroutine import coroutine
from MessagePassingMud.command.command_matcher import match_command
import json



@coroutine
def command_handler(p, conn, matcher = match_command):
    '''
        A coroutine that takes a string as an argument, matches them with the corresponding command, 
        and then executes that command with the given args, sending the results to the player that executed the command
    '''
    while True:
        msg = yield
        command, args = matcher(msg)
        result = command(p, args = args)
        for line in result:
            conn.push(line+"\n")
        conn.push(p.name+": "+msg+"\n")
        conn.push("Inventory: "+str(p.inventory)+"\n")
        
        
@coroutine
def json_command_handler(p, conn, matcher = match_command):
    '''
        A coroutine that takes a string as an argument, matches them with the corresponding command, 
        and then executes that command with the given args, sending the results to the player that executed the command
    '''
    while True:
        msg = yield
        command, args = matcher(msg)
        result = command(p, args = args)
        for item in result:
            conn.push(json.dumps(item))
        conn.push(json.dumps({"inv":p.get_inventory()}));    
        