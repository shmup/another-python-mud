'''
Created on Nov 24, 2011

@author: Nich
'''
from messanging import Messanger, Message
import command_utils
import async_commands

commands_dict = {
               "say": {
                       "class": async_commands.Say
                       },
               "mult": {
                        "class": async_commands.Mult
                        },
               
               }

class CommandPicker(Messanger):
    def process(self, m):
        command_args = command_utils.match_command(m.message, commands_dict)
        command = commands_dict[command_args[0]]
        args = command_args[1]
        comm = command["class"]()
        recip = m.recipients
        sender = m.sender
        comm.inbox.send(Message(sender, recip, args))



    
    
if __name__ == "__main__":
    pass
    
    
    
