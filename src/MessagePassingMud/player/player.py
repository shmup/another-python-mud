'''
Created on May 22, 2012

@author: Nich
'''

from map.directions import dirs, add_dirs
from map.game_map import dig
from physics.hittest import hit_test


class Player():
    def __init__(self, name = "", location = (0, 0), local_map = None):
        self.name = name
        self.location = location
        self.cache_map = {}
        self.local_map = local_map
        self.inventory = []
        self.upgrades = []
        self.gravity = -1
        self.velocity = 0
        self.account = None
        self.direction = "right"
    
    def set_account(self, account):
        self.account = account
    
    def get_account(self):
        return self.account
        
    def set_location(self, loc):
        x, y = loc
        if hit_test(self.location, loc, self.local_map):
            
            self.location = (x, y)
            return True
        return False
    
    def get_velocity(self):
        return self.velocity
    
    def get_effective_gravity(self):
        return self.gravity
        
    def move(self, dist, direction):
        if direction in dirs:
            if direction == "e":
                self.direction = "right"
            if direction == "w":
                self.direction = "left"
            
            num_dir = dirs[direction]
            for i in range(dist):
                new_loc = add_dirs(self.location, num_dir)
                if not self.set_location(new_loc):
                    return i
            return dist
        return 0
             
    def dig(self, dist, direction):
        if direction in dirs:
            if direction == "e":
                self.direction = "right"
            if direction == "w":
                self.direction = "left"
            
            num_dir = dirs[direction]
            for i in range(dist):
                new_loc = add_dirs(self.location, num_dir)
                gemstone = dig(new_loc, self.local_map)
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
        return self.inventory
    
    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)
    
    def get_upgrade_commands(self):
        upgrade_commands = {}
        for u in self.upgrades:
            for k, comm in u.commands_list.items():
                upgrade_commands[k] = comm
                
        return upgrade_commands
    
        