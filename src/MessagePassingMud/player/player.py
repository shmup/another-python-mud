'''
Created on May 22, 2012

@author: Nich
'''
from MessagePassingMud.map.game_map import gmap
from MessagePassingMud.map.directions import dirs, add_dirs
from MessagePassingMud.upgrades.jetpack import Jetpack


class Player():
    def __init__(self, name = "", location = (0, 0, 0)):
        self.name = name
        self.location = location
        self.local_map = gmap
        self.cache_map = {}
        self.inventory = [2]
        self.upgrades = []
        self.gravity = -1
        self.velocity = 0
        
    def set_location(self, loc):
        x, y, z = loc
        if self.local_map.get((x, y, z)) == 0 or \
           self.local_map.get(self.location) == 1:
            #i = 1
            #while self.local_map.get((x, y, z-i)) == 0: 
            #    i = i + 1
            #z = z - (i-1)
            self.location = (x, y, z)
            return True
        return False
    
    def get_velocity(self):
        return self.velocity
    
    def get_effective_gravity(self):
        return self.gravity
        
    def move(self, dist, direction):
        if direction in dirs:
            num_dir = dirs[direction]
            for i in range(dist):
                new_loc = add_dirs(self.location, num_dir)
                if not self.set_location(new_loc):
                    return i
            return dist
        return 0
             
    def dig(self, dist, direction):
        if direction in dirs:
            num_dir = dirs[direction]
            for i in range(dist):
                new_loc = add_dirs(self.location, num_dir)
                gemstone = gmap.dig(new_loc)
                if gemstone != 1 and gemstone != 0:
                    self.inventory.append(gemstone)
                if not self.set_location(new_loc):
                    return i
            return dist
        return 0
    
    def get_cache_map(self):
        return self.cache_map
    
    def set_cache_map(self, cmap):
        self.cache_map = cmap
    
    def set_local_map(self, l_map):
        self.local_map = l_map
    
    def get_location(self):
        return self.location
        
    def set_name(self, name):
        self.name = name
        
    def get_inventory(self):
        #new_dict = {}
        #num_sapp = self.inventory.count(2)
        #num_em = self.inventory.count(3)
        #if num_sapp > 0:
        #    new_dict["sapphire"] = num_sapp
        #if num_em > 0:
        #    new_dict["emerald"] = num_em
        return self.inventory
    
    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)
    
    def get_upgrade_commands(self):
        upgrade_commands = {}
        for u in self.upgrades:
            for k, comm in u.commands_list.items():
                upgrade_commands[k] = comm
                
        return upgrade_commands
        
        
default = Player("Nicholas", (0, 0, 1))
default.add_upgrade(Jetpack())

def get_default():
    return default

def get_all_players():
    return [get_default()]