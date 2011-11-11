'''
Created on Nov 9, 2011

@author: Nich
'''

import command_dict as com_list
import command_utils as com_utils
 

def command_factory(command_text, command_list = com_list.commands):
    split_text = com_utils.split_command(command_text)
    command_args = com_utils.match_command(split_text, command_list)
    command = command_list[command_args[0]]
    args = command_args[1]
    context = build_context(command, args)
    return (command, context)

def build_context(command, args):
    context = {}
    for req in command["requires"]:
        if req == "args":
            context[req] = args
        else:
            context[req] = get_requested_thing(req)
    return context

def get_requested_thing(req):
    return None        