'''
Created on May 22, 2012

@author: Nich
'''
from MessagePassingMud.utils.coroutine import coroutine
from MessagePassingMud.command.command_matcher import match_command

        
@coroutine
def command_handler(p, conn, matcher = match_command):
    while True:
        msg = yield
        command, args = matcher(p, msg)
        result = command(p, args = args)
        
        for item in result:
            dest, msg = item
            conn.push(dest, msg)
            
        