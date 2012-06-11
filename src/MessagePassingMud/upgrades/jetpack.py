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
            self.fuel = self.fuel - 1
            x, y, z = p.get_location()
            p.set_location((x, y, z+1))
            loc = p.get_location()
            return ("info", "You move 1 step to the up (Your position is: "+str(loc)+")"),
        else:
            self.fuel = 100
            return ("info", "You have run out of fuel. For Debug purposes, it has been set to 100 again"),
    
        
    
        