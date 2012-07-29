'''
Created on Jun 4, 2012

@author: Nich
'''

import random
import queue
mult = 1111
const = 125
#3677   3691   3697



def generate_mineral_vein(rand, start_chance, split_chance, extend_chance):
    def gen():
        seeds = queue.Queue()
        rand.randint(1, 100)
        while rand.randint(1, 100) < start_chance:
            pos = rand.randint(0, 49), rand.randint(0, 49)
            seeds.put(pos)
        
        minerals = {}
        while not seeds.empty():
            p = seeds.get()
            minerals[p] = 9
            if p[1] < 49 and p[0] > 0 and p[0] < 49:
                if rand.randint(1, 100) < extend_chance:
                    x, y = p
                    seeds.put((rand.randint(-1, 1)+x, 1+y))
                    if rand.randint(1, 100) < split_chance:
                        seeds.put((rand.randint(-1, 1)+x, 1+y))
            
        return minerals
    return gen
                        
                    
    

def map_neighbour_count(gmap, loc):
    if loc in gmap:
        acc = 0
        for n in neighbours(loc):
            x, y = n
            if (x, y) in gmap: 
                if gmap[(x, y)] > 0:
                    acc = acc+1
            else:
                acc = acc+1
        return acc
    return 0
        
        
        
def neighbour_count(gen, loc):
    acc = 0
    for n in neighbours(loc):
        x = loc[0]+n[0]  
        y = loc[1]+n[1]
        if(gen(x, y) == 1):
            acc = acc+1
        if acc >= 4:
            return True
        
#candidate for moving                
def neighbours(pos):
    for j in range(-1, 2):
        for i in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (i+pos[0], j+pos[1])


def generate(odds, i, j, offset=20):
    seed = str(i)+str(j)+str(offset)
    random.seed(seed)
    number = random.randint(1, odds)
    return 1 if number == 1 else 0

def generate_terrain(i, j, offset=20):
    kpart = ((offset*mult + const) % 3676)
    jpart = ((j*kpart + const) % 3691)
    ipart = ((i*jpart + const) % 3697)
     
    val = (ipart ^ jpart ^ kpart) %2
    return val

def generate_gemstone(i, j, offset = 20):
    sapp = 2 if generate(1000, i, j, offset) == 1 else 0
    em = 3 if generate(5000, i, j, offset) == 1 else 0
    rub = 4 if generate(10000, i, j, offset) == 1 else 0
    diam = 5 if generate(500000, i, j, offset) == 1 else 0
    
    return sapp or em or rub or diam or 0 

def generate_terrain_neighbours(i, j, offset, gen):
    nloc = (i, j)
    if neighbour_count(gen, nloc):
        return 1
    else:
        return gen(i, j, offset)


def generate_tile(i, j, offset = 20):
    gem = generate_gemstone(i, j, offset) 
    if gem >= 2:
        return gem
    return generate_terrain_neighbours(i, j, offset, generate_terrain) 
'''
def generate_sector(sector, size):
    sec_x, sec_y = sector
    x_size, y_size = size
    x_min, x_max = sec_x*x_size, sec_x*x_size+x_size
    y_min, y_max = sec_y*y_size, sec_y*y_size+y_size
    
    sector_map = {}
    for ny in range(y_min, y_max):
        for nx in range(x_min, x_max):
            nloc = (nx, ny)
            sector_map[nloc] = generate_tile(*nloc)
    
    return sector_map
'''
def generate_sector(sector, size):
    random.seed("This is a seed"+repr(sector))
    sec_x, sec_y = sector
    x_size, y_size = size
    x_min, x_max = sec_x*x_size, sec_x*x_size+x_size
    y_min, y_max = sec_y*y_size, sec_y*y_size+y_size
    
    sector_map = {}
    for ny in range(y_min, y_max):
        for nx in range(x_min, x_max):
            nloc = (nx, ny)
            sector_map[nloc] = 0 if random.randint(1, 100) < 15 else 1
    exp_map = fix_edges(sector_map, sector, size)        
    
    vein_gen = generate_mineral_vein(random, 80, 70, 50)
    minerals = vein_gen()
    
    
    
    for k, i in minerals.items():
        x, y = k
        
        exp_map[x+x_min, y+y_min] = i if exp_map[x+x_min, y+y_min] == 1 else exp_map[x+x_min, y+y_min]
    
    return exp_map

def fix_edges(sector_map, sector, size):
    
    new_map = {}
    for k in sector_map.keys():
        nx, ny = k
        if map_neighbour_count(sector_map, (nx, ny)) > 5:
            new_map[(nx, ny)] = 1
        else:
            new_map[(nx, ny)] = 0
    return new_map
            
             


if __name__ == "__main__":
    sector = (1, 1)
    size = (50, 50)
    sector_map = generate_sector(sector, size)
    sec_x, sec_y = sector
    x_size, y_size = size
    x_min, x_max = sec_x*x_size, sec_x*x_size+x_size
    y_min, y_max = sec_y*y_size, sec_y*y_size+y_size
    for ny in range(y_min, y_max):
        line = ""
        for nx in range(x_min, x_max):
            line += str(sector_map[(nx, ny)])
        print(line)
            
