'''
Created on Jun 7, 2012

@author: Nich
'''



#candidate for moving
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
#candidate for moving                
def neighbours(pos):
    for k in range(-1, 2):
        for j in range(-1, 2):
            for i in range(-1, 2):
                if (i, j, k) == (0, 0, 0):
                    continue
                yield (i+pos[0], j+pos[1], k+pos[2])


def generate(pos, size, gamemap):
    gen_map = {}
    for k in range(size[2]):
        for j in range(size[1]):
            for i in range(size[0]):
                gen_map[(i, j, k)] = gamemap.get((i, j, k))
    return gen_map
    
def generate_blind(pos, size, gamemap):
    bounds = ((pos[0] - int(size[0] / 2), pos[0] + int(size[0] / 2)), (pos[1] - int(size[1] / 2), pos[1] + int(size[1] / 2)), (pos[2] - int(size[2] / 2), pos[2] + int(size[2] / 2)))        
    gen_map = {}
    generate_blind_recur(pos, gen_map, bounds, [], gamemap)
    return gen_map
    
            
def generate_blind_recur(pos, gen_map, bounds, visited, gamemap):
    if pos[0] > bounds[0][0] and pos[0] < bounds[0][1] and \
       pos[1] > bounds[1][0] and pos[1] < bounds[1][1] and \
       pos[2] > bounds[2][0] and pos[2] < bounds[2][1]:
        
        gen_map[pos] = gamemap.get(pos)
        
        if gen_map[pos] == 0 or visited == []:
            for n in neighbours(pos):
                if n not in visited:
                    visited.append(n)
                    generate_blind_recur(n, gen_map, bounds, visited, gamemap)
