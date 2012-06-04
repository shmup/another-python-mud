'''
Created on May 22, 2012

@author: Nich
'''

from MessagePassingMud.map import cave_gen


def generate_map(gmap):
    print("Loading map")
    if gmap is None:
        gmap = cave_gen.generate((0, 0, 0), (5, 5, 5), cave_gen.generate_value)
        gmap = cave_gen.apply_automata(gmap, cave_gen.automaton_10_18)
        #gmap = cave_gen.apply_automata(gmap, cave_gen.automaton_14_18)
    print("Map loaded")
    return gmap

#cache_map = generate_map(None)


    


def display_horizontal(g_map, pos, ran):
    z = pos[2]
    xmin = pos[0] - int(ran[0]/2)
    xmax = pos[0] + int(ran[0]/2)
    ymin = pos[1] - int(ran[1]/2)
    ymax = pos[1] + int(ran[1]/2)
    yield "0"*(ran[1]+2)
    for i in range(xmin, xmax+1):
        line = "0"
        for j in range(ymin, ymax+1):
            if (i, j, z) == pos:
                line += '@'
            elif g_map[i][j][z] == -1:
                line += '0'
            elif g_map[i][j][z] == 1:
                line += "#"
            elif g_map[i][j][z] == 0:
                line += " "
        yield line+"0"
    yield "0"*(ran[1]+2)

def display_vertical(g_map, pos, ran):
    x = pos[0]
    zmin = pos[2] - int(ran[1]/2)
    zmax = pos[2] + int(ran[1]/2)
    ymin = pos[1] - int(ran[0]/2)
    ymax = pos[1] + int(ran[0]/2)
    yield "0"*(ran[1]+2)
    for y in range(ymin, ymax+1):
        line = "0"
        for z in range(zmin, zmax+1):
            if (x, y, z) == pos:
                line += '@'
            else:
                line += ('#' if g_map[x][y][z] else " ")
        yield line+"0"
    yield "0"*(ran[1]+2)


'''
def show_map(p = None, size = (23, 49), args = None):
    pos = None
    if not p is None:
        pos = p.location
    else:
        pos = (3, 3, 3)
    gen_hoz = display_horizontal(cache_map, pos, size)
    gen_vert = display_vertical(cache_map, pos, size)
    for line in compose(gen_hoz, gen_vert):
        yield line
        
        
if __name__ == "__main__":
    for line in show_map(size = (3, 3)):
        print(line)
'''    