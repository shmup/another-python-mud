'''
Created on Jun 3, 2012

@author: Nich
'''

from map.map_display_functions import generate
from data.data_store import DataStore
from itertools import chain



class GameMap(object):
    '''
    
    '''
    def __init__(self, gen_sec, db):
        self.db = db
        self.gen_sec = gen_sec
        self.map_cache = {}
        self.sector = {}
        self.sector_size = (50, 50)
    
    
    def set(self, loc, val): #@ReservedAssignment
        self.map_cache[loc] = val
        #set_stored_value(loc, val)
    
    def get(self, loc):
        if not loc in self.map_cache:
            self.generate_sector(loc, self.sector_size)
        
        return self.map_cache[loc]
            
    def merge_map(self, val):
        self.map_cache = dict(chain(self.map_cache.items(), val.items()))

    def generate_sector(self, loc, size):
        x, y = loc
        x_size, y_size = size
        
        from math import floor
        sector = (floor(x/x_size), floor(y/y_size))
        sec_x, sec_y = sector
        x_min, x_max = sec_x*x_size, sec_x*x_size+x_size
        y_min, y_max = sec_y*y_size, sec_y*y_size+y_size
        
        if not sector in self.sector:
            sector_map = self.gen_sec(sector, size)
            self.merge_map(sector_map)
            val = self.db.get_stored_range(x_min, x_max, y_min, y_max)
            self.merge_map(val)
                
    

def dig(loc, game_map):
        if(game_map.get(loc) == 0):
            return 0
        else:
            prev = game_map.get(loc) 
            game_map.set(loc, 0)
            game_map.db.set_stored_value(loc, 0)
            return prev



def show_map(p, size = (33, 20), args = None):
    pos = p.location
    cache_map = generate(pos, size, DataStore.instance().data["game_map"])
    norm_map = normalize(cache_map, p.get_location(), size)
    diff_map = diff(p.cache_map, norm_map)
    p.set_cache_map(norm_map)
    
    return ("gamemap", {"map": diff_map, "dir":p.direction}),
    
    
import math
def normalize(gamemap, pos, map_size):
    new_map = {}
    xpos, zpos = pos
    z_size = math.ceil(map_size[1]/2)
    x_size = math.floor(map_size[0]/2)
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
    
    
    
      
        
