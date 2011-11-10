'''
Created on Nov 10, 2011

@author: Nich
'''
import command.command_dict as comm_dict

def merge_text(command, num):
    #merges the first num elements of command
    cmd = " ".join(command[0:num+1])
    return cmd


def split_command(command_text):
    command = command_text.split()
    return command

def match_command(split_command_text, comm = comm_dict.commands):    
    for i in reversed(range(len(split_command_text))):
        cmd = merge_text(split_command_text, i)
        if cmd in comm:
            return " ".join(split_command_text[0:i+1]), " ".join(split_command_text[i+1:])