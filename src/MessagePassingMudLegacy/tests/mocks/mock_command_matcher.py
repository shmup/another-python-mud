'''
Created on Jun 4, 2012

@author: Nich
'''
def match_command(p, msg):
    return (lambda p, args:(("info", "executing "+args[0]+" with arguments "+" ".join(args[1:])),), msg.split(" "))