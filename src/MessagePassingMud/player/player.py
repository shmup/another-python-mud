'''
Created on May 22, 2012

@author: Nich
'''

from map.directions import dirs, add_dirs
from map.game_map import dig as map_dig
from physics.hittest import hit_test
from data.tiles import tiles, get_tile_property

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
    
    def dig(self, direction):
        self.set_direction(direction)
        
        new_location = get_new_location(self, direction)
        new_tile = map_dig(new_location, self.local_map)
        old_tile = self.local_map.get(self.location)
        on_enter = get_tile_property(tiles, new_tile, "on_enter")
        on_exit = get_tile_property(tiles, old_tile, "on_exit")
        if on_exit:
            on_exit(old_tile, self)
        self.set_location(new_location)
        if on_enter:
            on_enter(new_tile, self)
    
    def set_direction(self, direction):
        if(direction == "e"):
            self.direction = "right"
        if(direction == "w"):
            self.direction = "left"
        if(direction == "d"):
            self.direction = "down"
        if(direction == "u"):
            self.direction = "up"    
    
    def move(self, direction):
        self.set_direction(direction)
        new_location = get_new_location(self, direction)
        if hit_test(self.location, new_location, self.local_map):
            new_tile = self.local_map.get(new_location)
            old_tile = self.local_map.get(self.location)
            on_enter = get_tile_property(tiles, new_tile, "on_enter")
            on_exit = get_tile_property(tiles, old_tile, "on_exit")
            if on_exit:
                on_exit(self)
            self.set_location(new_location)
            if on_enter:
                on_enter(self)
            return True
        else:
            return False
    
    def set_account(self, account):
        self.account = account
    
    def get_account(self):
        return self.account
        
    def set_location(self, loc):
        self.location = loc
        
    def get_velocity(self):
        return self.velocity
    
    def get_effective_gravity(self):
        return self.gravity
        
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
    
'''
def move(p, dist, direction):
    if direction in dirs:
        
        if direction == "e":
            p.direction = "right"
        if direction == "w":
            p.direction = "left"
        
        
        num_dir = dirs[direction]
        for i in range(dist):
            new_loc = add_dirs(p.location, num_dir)
            if not p.set_location(new_loc):
                return i
        return dist
    return 0
'''

         
   
def get_new_location(p, direction):
    if direction in dirs:
        num_dir = dirs[direction]
        new_loc = add_dirs(p.location, num_dir)
        return new_loc
    else:
        return p.location
'''                
def dig(p, direction):
    if direction in dirs:
        
        if direction == "e":
            p.direction = "right"
        if direction == "w":
            p.direction = "left"
        
        num_dir = dirs[direction]
        for i in range(dist):
            new_loc = add_dirs(p.location, num_dir)
            tile = map_dig(new_loc, p.local_map)
            blocked = not p.set_location(new_loc)    
            if blocked:
                return i
            else:
                enter_func = get_tile_property(tiles, tile, "on_enter")
                
        return dist
    return 0
'''       