'''
Created on May 22, 2012

@author: Nich
'''
from MessagePassingMud.command.commands import *
from MessagePassingMud.map.game_map import show_map





def match_command(msg):
    
    #We can and have done better then this. No excuses, fix this
    if msg[0:3] == "say":
        return say, msg[3:].split(" ")
    if msg[0:4] == "goto":
        return goto, msg[5:].split(" ")
    if msg[0:1] == "n":
        return n, None
    if msg[0:1] == "s":
        return s, None
    if msg[0:1] == "e":
        return e, None
    if msg[0:1] == "w":
        return w, None
    
    return show_map, (None)