'''
Created on May 22, 2012

@author: Nich
'''
from MessagePassingMud.command.commands import *
from MessagePassingMud.map.game_map import show_map


commands = {"say":{"function":say, "num_args":"unlimited"},
            "move":{"function":move, "num_args":2},
            "dig":{"function":dig, "num_args":2},
            "goto":{"function":goto, "num_args":3},
            "n":{"function":n, "num_args":0},
            "s":{"function":s, "num_args":0},
            "e":{"function":e, "num_args":0},
            "w":{"function":w, "num_args":0},
            "l":{"function":show_map, "num_args":0}
            }


def match_command(msg, comms = commands):
    split_msg = msg.split(" ")
    comm_name = split_msg[0]
    if comm_name in comms:
        command = comms[comm_name]
        num_args = command["num_args"]
        # If the number of args is unlimited, or the correct number
        if num_args == "unlimited" or num_args == len(split_msg[1:]):
            return command["function"], split_msg[1:]
    
    return default_message, None


def default_message(p = None, args = None):
    return ("Sorry, I don't understand that",)