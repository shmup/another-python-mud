'''
Created on Jun 4, 2012

@author: Nich
'''
def match_command(msg):
    return (lambda p, args:(("executing "+args[0]+" with arguments "+" ".join(args[1:])),), msg.split(" "))