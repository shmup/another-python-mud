'''
Created on May 22, 2012

@author: Nich
'''






#p is the current player, msg is the command entered, and comms is a list of dictionaries containing commands to match
def match_command(p, msg, comms):
    split_msg = msg.split(" ")
    comm_name = split_msg[0]
    for command_list in comms:
        if comm_name in command_list:
            command = command_list[comm_name]
            num_args = command["num_args"]
            # If the number of args is unlimited, or the correct number
            if num_args == "unlimited" or num_args == len(split_msg[1:]):
                return command["function"], split_msg[1:]
    
    return default_message, None


def default_message(p = None, args = None):
    return ("info", "Sorry, I don't understand that"),