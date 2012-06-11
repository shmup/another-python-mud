'''
Created on Jun 3, 2012

@author: Nich
'''
from MessagePassingMud.map.map_generators import generate_tile
from MessagePassingMud.map.map_generation_functions import generate_blind, neighbour_count 
from MessagePassingMud.map.start_ship import generate_starting_ship




class GameMap(object):
    '''
    
    '''
    def __init__(self):
        self.gen = generate_tile
        self.map_cache = generate_starting_ship((0, 0, 0))
    
    def dig(self, loc):
        prev = self.get(loc) 
        self.map_cache[loc] = 0
        return prev
    
    
    def get(self, loc):
        if loc in self.map_cache:
            return self.map_cache[loc]
        else:
            if neighbour_count(self.gen, loc):
                self.map_cache[loc] = 1
            else:
                self.map_cache[loc] = self.gen(*loc)
            return self.map_cache[loc]
            
    
gmap = GameMap()


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
    
    
    
      
        
