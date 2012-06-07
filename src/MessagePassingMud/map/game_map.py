'''
Created on Jun 3, 2012

@author: Nich
'''
from MessagePassingMud.map.map_generators import generate_tile



def neighbour_count(gen, loc):
    acc = 0
    for n in neighbours(loc):
        x = loc[0]+n[0]  
        y = loc[1]+n[1]
        z = loc[2]+n[2]
        if(gen(x, y, z) == 1):
            acc = acc+1
        if acc >= 13:
            return True
                
def neighbours(pos):
    for k in range(-1, 2):
        for j in range(-1, 2):
            for i in range(-1, 2):
                if (i, j, k) == (0, 0, 0):
                    continue
                yield (i+pos[0], j+pos[1], k+pos[2])


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
            
    def generate(self, size):
        gen_map = {}
        for k in range(size[2]):
            for j in range(size[1]):
                for i in range(size[0]):
                    gen_map[(i, j, k)] = self.get((i, j, k))
        return gen_map
    
    def generate_blind(self, pos, size):
        bounds = ((pos[0]-int(size[0]/2), pos[0]+int(size[0]/2)),(pos[1]-int(size[1]/2), pos[1]+int(size[1]/2)),(pos[2]-int(size[2]/2), pos[2]+int(size[2]/2)))        
        gen_map = {}
        self.generate_blind_recur(pos, gen_map, bounds, [])
        return gen_map
        
                
    def generate_blind_recur(self, pos, gen_map, bounds, visited):
        if pos[0] > bounds[0][0] and pos[0] < bounds[0][1] and \
           pos[1] > bounds[1][0] and pos[1] < bounds[1][1] and \
           pos[2] > bounds[2][0] and pos[2] < bounds[2][1]:
            
            gen_map[pos] = self.get(pos)
            
            if gen_map[pos] == 0 or visited == []:
                for n in neighbours(pos):
                    if n not in visited:
                        visited.append(n)
                        self.generate_blind_recur(n, gen_map, bounds, visited)
        

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


def show_map(p = None, size = (20, 20), args = None):
    pos = None
    if not p is None:
        pos = p.location
    else:
        pos = (3, 3, 3)
    
    cache_map = gmap.generate_blind(pos, (12, 12, 12))
    gen_vert_x = display_vertical_x(cache_map, pos, size)
    
    for line in gen_vert_x:
        yield line
    
    

if __name__ == "__main__":
    for i in show_map():
        print(i)
    
    
    
      
        
