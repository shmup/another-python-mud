'''
Created on Jun 3, 2012

@author: Nich
'''

from map.map_generation_functions import generate_blind, generate_flashlight, generate
from map.start_ship import generate_starting_ship
#get_stored_value, get_stored_range, set_stored_value, dump_map_to_db
from data.data_store import DataStore
from itertools import chain


class GameMap(object):
    '''
    
    '''
    def __init__(self, gen, db):
        self.db = db
        self.gen = gen
        self.map_cache = {}#generate_starting_ship((0, 0, 0))
        self.sector = {}
        self.sector_size = (50, 50)
    
    def dig(self, loc):
        if(self.get(loc) == 0):
            return 0
        else:
            prev = self.get(loc) 
            self.set(loc, 0)
            self.db.set_stored_value(loc, 0)
            return prev
    
    def set(self, loc, val): #@ReservedAssignment
        self.map_cache[loc] = val
        #set_stored_value(loc, val)
    
    def get(self, loc):
        if not loc in self.map_cache:
            self.cache_next(loc, self.sector_size)
        
        return self.map_cache[loc]
            
            
    def cache_next(self, loc, size):
        x, y = loc
        x_size, y_size = size
        
        from math import floor
        sector = (floor(x/x_size), floor(y/y_size))
        sec_x, sec_y = sector
        
        if not sector in self.sector:
            x_min, x_max = sec_x*x_size, sec_x*x_size+x_size
            y_min, y_max = sec_y*y_size, sec_y*y_size+y_size
            
            
            for ny in range(y_min, y_max):
                for nx in range(x_min, x_max):
                    nloc = (nx, ny)
                    self.set(nloc, self.gen(*nloc))
            
            val = self.db.get_stored_range(x_min, x_max, y_min, y_max)
            self.map_cache = dict(chain(self.map_cache.items(), val.items()))
            self.sector[sector] = 1        
        
    def dump_to_db(self):
        d_map = []
        for key, value in self.map_cache.items():
            x, y = key
            d_map.append((x, y, value))
        return d_map
    


def show_map(p = None, size = (33, 19), args = None):
    pos = None
    if not p is None:
        pos = p.location
    else:
        pos = (3, 3, 3)
    
    
        
    cache_map = generate(pos, (32, 18), DataStore.instance().data["game_map"])
    
    #cache_map = generate_blind(pos, (12, 12, 12), DataStore.instance().data["game_map"])
    
    norm_map = normalize(cache_map, p.get_location(), size)
    diff_map = diff(p.cache_map, norm_map)
    p.set_cache_map(norm_map)
    #gen_vert_x = display_vertical_x(cache_map, pos, size)
    
    yield ("gamemap", diff_map)
    #for line in gen_vert_x:
        #yield line
    

def normalize(gamemap, pos, map_size):
    new_map = {}
    xpos, zpos = pos
    z_size = int(map_size[1]/2)
    x_size = int(map_size[0]/2)
    for key, _value in gamemap.items():
        x, z = key
        str_key = str(x-xpos+x_size)+"_"+str(z-zpos+z_size) 
        new_map[str_key] = gamemap[key]
    return new_map
    
def diff(dict1, dict2):
    new_dict = {}
    for key, value in dict2.items():
        if key not in dict1:
            new_dict[key] = value
        elif dict1[key] != dict2[key]:
            new_dict[key] = value
    return new_dict


if __name__ == "__main__":
    for i in show_map():
        print(i)
    
    
    
      
        
