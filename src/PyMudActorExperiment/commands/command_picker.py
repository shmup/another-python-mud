'''
Created on Nov 20, 2011

@author: Nich
'''
from coroutine import coroutine
import command_utils
import commands.commands as commands

commands_dict = {
               "say": {
                       "function": commands.say
                       },
               "mult": {
                        "function": commands.mult
                        },
               
               }

@coroutine
def command_picker(inbox):
    while True:
        message = (yield)
        command_args = command_utils.match_command(message["args"], commands_dict)
        command = commands_dict[command_args[0]]
        args = command_args[1]
        comm = command["function"](inbox)
        targets = message["targets"]
        sender = message["sender"]
        comm.send({"sender":sender, "targets":targets, "args":args})
        