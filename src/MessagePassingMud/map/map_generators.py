'''
Created on Jun 4, 2012

@author: Nich
'''

import random
mult = 1111
const = 125
#3677   3691   3697

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


if __name__ == "__main__":
    k = 0
    for j in range(100):
        line = ""
        for i in range(100):
            line += str(generate_gemstone(i, j))
        print(line)

