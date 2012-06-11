'''
Created on Jun 4, 2012

@author: Nich
'''

class Connection():
    
    def __init__(self):
        self.msgs = []
    
    def push(self, dest, msg):
        self.msgs.append((dest, msg))
        
    