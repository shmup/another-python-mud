'''
Created on Jun 3, 2012

@author: Nich
'''
from MessagePassingMud.map.map_generators import generate_tile
from MessagePassingMud.map.map_generation_functions import generate_blind, neighbour_count 





class GameMap(object):
    '''
    
    '''
    def __init__(self):
        self.gen = generate_tile
        self.map_cache = {}
    
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
            
    
        

colors = {
          "blue": chr(27)+"[34m",
          "cyan": chr(27)+"[36m",
          "white": chr(27)+"[37m",
          "red": chr(27)+"[31m",
          "green": chr(27)+"[32m",
          "yellow": chr(27)+"[33m",
          }        

current_color = "white"
def set_color(color):
    global current_color
    if color == current_color or not color in colors:
        return ""
    else:
        current_color = color
        return colors[color]         
        


def display_vertical_x(g_map, pos, ran):
    y = pos[1]
    zmin = pos[2] - int(ran[1]/2)
    zmax = pos[2] + int(ran[1]/2)
    xmin = pos[0] - int(ran[0]/2)
    xmax = pos[0] + int(ran[0]/2)
    yield "0"*(ran[0]+2)
    for z in range(zmax, zmin, -1):
        line = "0"
        for x in range(xmin, xmax):
            
            if (x, y, z) == pos:
                line += set_color("red")+'@'
            elif (x, y, z) not in g_map:
                line += set_color("white")+'?'
            elif g_map[(x, y, z)] >= 2:
                line += set_color("yellow")+"0"
            elif g_map[(x, y, z)] == 1:
                line += set_color("blue")+"#"
            elif g_map[(x, y, z)] == 0:
                line += " " if g_map[(x, y-1, z)] == 0 else set_color("cyan")+"#"
        yield line+set_color("white")+"0"
    yield "0"*(ran[0]+2)



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
    
    yield {"gamemap":diff_map}
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
    
    
    
      
        
