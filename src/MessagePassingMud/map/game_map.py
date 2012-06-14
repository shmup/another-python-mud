'''
Created on Jun 3, 2012

@author: Nich
'''
from MessagePassingMud.map.map_generators import generate_tile
from MessagePassingMud.map.map_generation_functions import generate_blind, neighbour_count 
from MessagePassingMud.map.start_ship import generate_starting_ship
from MessagePassingMud.model.data_map import get_stored_value, set_stored_value, dump_map_to_db



class GameMap(object):
    '''
    
    '''
    def __init__(self):
        self.gen = generate_tile
        self.map_cache = generate_starting_ship((0, 0, 0))
    
    def dig(self, loc):
        if(self.get(loc) == 0):
            return 0
        else:
            prev = self.get(loc) 
            self.set(loc, 0)
            set_stored_value(loc, 0)
            return prev
    
    def set(self, loc, val): #@ReservedAssignment
        self.map_cache[loc] = val
        #set_stored_value(loc, val)
    
    def get(self, loc):
        if loc in self.map_cache:
            return self.map_cache[loc]
        
        val = get_stored_value(loc)
        if  val != None:
            self.map_cache[loc] = val
            return val
        
        else:
            if neighbour_count(self.gen, loc):
                self.set(loc, 1)
            else:
                self.set(loc, self.gen(*loc))
            return self.map_cache[loc]
    def dump_to_db(self):
        d_map = []
        for key, value in self.map_cache.items():
            x, y, z, = key
            d_map.append((x, y, z, value))
        return d_map
    
gmap = GameMap()

def dump_to_db():
    dump_map_to_db(gmap.dump_to_db())


def show_map(p = None, size = (33, 19), args = None):
    pos = None
    if not p is None:
        pos = p.location
    else:
        pos = (3, 3, 3)
    
    cache_map = generate_blind(pos, (12, 12, 12), gmap)
    norm_map = normalize(cache_map, p.get_location(), size)
    diff_map = diff(p.cache_map, norm_map)
    p.set_cache_map(norm_map)
    #gen_vert_x = display_vertical_x(cache_map, pos, size)
    
    yield ("gamemap", diff_map)
    #for line in gen_vert_x:
        #yield line
    

def normalize(gamemap, pos, map_size):
    new_map = {}
    print(pos)
    xpos, ypos, zpos = pos
    z_size = int(map_size[1]/2)
    x_size = int(map_size[0]/2)
    
    for key, _value in gamemap.items():
        x, y, z = key
        if y == ypos:
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
    
    
    
      
        
