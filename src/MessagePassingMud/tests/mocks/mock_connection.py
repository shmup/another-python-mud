'''
Created on Jun 4, 2012

@author: Nich
'''

class Connection():
    
    def __init__(self):
        self.msgs = []
    
    def push(self, msg):
        self.msgs.append(msg)
        
    