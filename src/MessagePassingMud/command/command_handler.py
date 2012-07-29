'''
Created on May 22, 2012

@author: Nich
'''
from utils.coroutine import coroutine
from command.command_matcher import match_command
from command.commands import *
from map.game_map import show_map

commands = {
            "say":{"function":say, "num_args":"unlimited"},
            "move":{"function":move, "num_args":1},
            "dig":{"function":dig, "num_args":1},
            "goto":{"function":goto, "num_args":3},
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
            
        