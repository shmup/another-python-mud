'''
Created on May 22, 2012

@author: Nich
'''
from MessagePassingMud.map.game_map import gmap


class Player():
    def __init__(self, name = "", location = (0, 0, 0)):
        self.name = name
        self.location = location
        self.local_map = gmap
        
    def set_location(self, loc):
        x, y, z = loc
        if self.local_map.get((x, y, z)) == 0 or \
           self.local_map.get(self.location) == 1:
            i = 1
            while self.local_map.get((x, y, z-i)) == 0: 
                i = i + 1
            z = z - (i-1)
            self.location = (x, y, z)
            return True
        return False
        
    
    def set_local_map(self, l_map):
        self.local_map = l_map
    
    def get_location(self):
        return self.location
        
    def set_name(self, name):
        self.name = name
        
        
default = Player("Nicholas", (24, 48, 0))

def get_default():
    return default