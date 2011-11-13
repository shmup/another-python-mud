'''
Created on Nov 10, 2011

@author: Nich
'''
import command.command_functions as c

commands = {
            "say": {
                    "requires": ["sender", "local_area_targets", "args"],
                    "function": c.say,
                    
                    },
            "default": {
                        "requires":["sender"],
                        "function":c.default
                        },
            "default": {
                        "requires":[],
                        "function":c.com_close
                        },
            
            }



