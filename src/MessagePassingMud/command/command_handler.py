'''
Created on May 22, 2012

@author: Nich
'''
from utils.coroutine import coroutine
from command.command_matcher import match_command
from command.commands import *


commands = {"say":{"function":say, "num_args":"unlimited"},
            "move":{"function":move, "num_args":2},
            "dig":{"function":dig, "num_args":2},
            "goto":{"function":goto, "num_args":3},
            "out":{"function":n, "num_args":0},
            "in":{"function":s, "num_args":0},
            "e":{"function":e, "num_args":0},
            "w":{"function":w, "num_args":0},
            "l":{"function":show_map, "num_args":0}
            }

        
@coroutine
def command_handler(p, conn, matcher = match_command, command_set = None):
    
    while True:
        msg = yield
        
        #debug line, should refactor
        c_s = [commands, p.get_upgrade_commands()] if command_set == None else command_set
        
        command, args = matcher(p, msg, c_s)
        result = command(p, args = args)
        
        for item in result:
            dest, msg = item
            conn.push(dest, msg)
            
        