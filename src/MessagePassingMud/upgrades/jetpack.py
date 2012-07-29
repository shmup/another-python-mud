'''
Created on Jun 10, 2012

@author: Nich
'''

class Jetpack(object):
    '''
    classdocs
    '''
    
    def __init__(self, fuel = 100):
        self.fuel = fuel
        self.commands_list = {"up":{"function":self.up, "num_args":0},}
        
        
    def up(self, p, args = None):
        if self.fuel != 0:
            p.move("u")
            self.fuel = self.fuel - 1
            return ("info", "You move 1 step to the up (Your position is: "+str(p.get_location())+")"),
        else:
            self.fuel = 100
            return ("info", "You have run out of fuel. For Debug purposes, it has been set to 100 again"),
    
        
    
        