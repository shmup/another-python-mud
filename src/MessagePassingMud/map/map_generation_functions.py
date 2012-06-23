'''
Created on Jun 7, 2012

@author: Nich
'''



from map_generators import neighbours

def generate(pos, size, gamemap):
    x, y = pos
    len_x, len_y = size
    
    gen_map = {}
    
    for j in range(y - int(len_y/2), y + int(len_y/2)):
        for i in range(x - int(len_x/2), x + int(len_x/2)):
            gen_map[(i, j)] = gamemap.get((i, j))
    return gen_map
    
def generate_blind(pos, size, gamemap):
    bounds = ((pos[0] - int(size[0] / 2), pos[0] + int(size[0] / 2)), (pos[1] - int(size[1] / 2), pos[1] + int(size[1] / 2)))        
    gen_map = {}
    generate_blind_recur(pos, gen_map, bounds, [], gamemap)
    return gen_map
    
            
def generate_blind_recur(pos, gen_map, bounds, visited, gamemap):
    if pos[0] > bounds[0][0] and pos[0] < bounds[0][1] and \
       pos[1] > bounds[1][0] and pos[1] < bounds[1][1]:
        
        gen_map[pos] = gamemap.get(pos)
        
        if gen_map[pos] == 0 or visited == []:
            for n in neighbours(pos):
                if n not in visited:
                    visited.append(n)
                    generate_blind_recur(n, gen_map, bounds, visited, gamemap)

def generate_flashlight(pos, direction, size, gamemap):
    num_dir = -1 if direction == "left" else 1
    x, z = pos
    gen_map = {}
    for i in range(size):
        curr_size = i
        for j in range(curr_size):
            curr_x = x+(i*num_dir)
            curr_z = z+j
            curr_pos = (curr_x, curr_z)
            tile = gamemap.get(curr_pos)
            gen_map[curr_pos] = tile
            if tile >= 1 and tile <= 100:
                break
    return gen_map
