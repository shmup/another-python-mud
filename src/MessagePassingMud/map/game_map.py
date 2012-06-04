'''
Created on Jun 3, 2012

@author: Nich
'''
from cave_gen import generate_value
from MessagePassingMud.utils.compose import compose


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
        self.gen = generate_value
        self.map_cache = {}
    
    def dig(self, loc):
        self.map_cache[loc] = 0
    
    
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
        

        
def display_horizontal(g_map, pos, ran):
    z = pos[2]
    xmin = pos[0] - int(ran[0]/2)
    xmax = pos[0] + int(ran[0]/2)
    ymin = pos[1] - int(ran[1]/2)
    ymax = pos[1] + int(ran[1]/2)
    yield "0"*(ran[0]+2)
    for j in range(ymax, ymin, -1):
        line = "0"
        for i in range(xmin, xmax):
            if (i, j, z) == pos:
                line += '@'
            elif (i, j, z) not in g_map:
                line += '?'
            elif g_map[(i, j, z)] == 1:
                line += "#"
            elif g_map[(i, j, z)] == 0:
                line += " "
        yield line+"0"
    yield "0"*(ran[0]+2)

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
                line += '@'
            elif (x, y, z) not in g_map:
                line += '?'
            elif g_map[(x, y, z)] == 1:
                line += "#"
            elif g_map[(x, y, z)] == 0:
                line += " "
        yield line+"0"
    yield "0"*(ran[0]+2)

def display_vertical_y(g_map, pos, ran):
    x = pos[0]
    zmin = pos[2] - int(ran[1]/2)
    zmax = pos[2] + int(ran[1]/2)
    ymin = pos[1] - int(ran[0]/2)
    ymax = pos[1] + int(ran[0]/2)
    yield "0"*(ran[0]+2)
    for z in range(zmax, zmin, -1):
        line = "0"
        for y in range(ymin, ymax):
            if (x, y, z) == pos:
                line += '@'
            elif (x, y, z) not in g_map:
                line += '?'
            elif g_map[(x, y, z)] == 1:
                line += "#"
            elif g_map[(x, y, z)] == 0:
                line += " "
        yield line+"0"
    yield "0"*(ran[0]+2)

gmap = GameMap()


def show_map(p = None, size = (20, 20), args = None):
    pos = None
    if not p is None:
        pos = p.location
    else:
        pos = (3, 3, 3)
    
    
    cache_map = gmap.generate_blind(pos, (12, 12, 12))
    gen_hoz = display_horizontal(cache_map, pos, size)
    gen_vert_x = display_vertical_x(cache_map, pos, size)
    gen_vert_y = display_vertical_y(cache_map, pos, size)
    for line in compose(gen_hoz, gen_vert_x, gen_vert_y):
        yield line
            

if __name__ == "__main__":
    for i in show_map():
        print(i)
    
    
    
      
        
