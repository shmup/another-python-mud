'''
Created on Nov 16, 2011

@author: Nich
'''
'''
[[[[1]]]]
[[[2, 2],[2, 2]],[[2, 2],[2, 2]]]

'''

import random
mult = 1111
const = 125
#3677   3691   3697


def generate_value(i, j, k):
    kpart = ((k*mult + const) % 3676)
    jpart = ((j*kpart + const) % 3691)
    ipart = ((i*jpart + const) % 3697)
     
    val = (ipart ^ jpart ^ kpart) %2
    return val

def generate(to, fro, generator):
    delta = [fro[i] - to[i] for i in range(len(to))]
    delta = [abs(d) for d in delta]
    gen_map = []
    for i in range(delta[0]):
        gen_map.append([])
        for j in range(delta[1]):
            gen_map[i].append([])
            for k in range(delta[2]):
                val = generator(i, j, k)
                gen_map[i][j].append(val)
    return gen_map
   


def calculate_dimensionality(nd_map, results):
    #if the elements of map are arrays, call them recursively
    #else return
    if isinstance(nd_map, list):
        results.append(len(nd_map))
        calculate_dimensionality(nd_map[0], results)
        return results
    else:
        return results
    
def calculate_order(nd_map, results):
    return len(calculate_dimensionality(nd_map, results))

def display_horizontal(g_map, pos, ran):
    z = pos[2]
    xmin = pos[0] - int(ran/2)
    xmax = pos[0] + int(ran/2)
    ymin = pos[1] - int(ran/2)
    ymax = pos[1] + int(ran/2)
    print("0"*(ran+3))
    for i in range(xmin, xmax+1):
        line = "0"
        for j in range(ymin, ymax+1):
            line += ('#' if g_map[i][j][z] else " ")
        print(line+"0")
    print("0"*(ran+3))        

def generateNeighboursList():
    l = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if not (x == 0 and y == 0 and z == 0):
                    l.append((x, y, z))
    return l
                    
    
def automaton_14_18(pos, gmap, neighbours_list):
    acc = 0
    for i in neighbours_list:
        x = pos[0] + i[0]
        y = pos[1] + i[1]
        z = pos[2] + i[2]
        if x < 0: x = 0
        if y < 0: y = 0
        if z < 0: z = 0
        if x >=50: x = 49
        if y >= 50: y = 49
        if z >= 50: z = 49
        if gmap[x][y][z] == 1:
            acc = acc+1
        if acc >= 12:
            return 1
    return 0

def apply_automata(gmap, automaton):
    neighbours_list = generateNeighboursList()
    newmap = []
    for i in range(len(gmap)):
        newmap.append([])
        for j in range(len(gmap[i])):
            newmap[i].append([])
            for k in range(len(gmap[i][j])):
                newmap[i][j].append(automaton((i, j, k), gmap, neighbours_list))
    return newmap
    

if __name__ == '__main__':
    gmap = generate((0, 0, 0), (50, 50, 50), generate_value) 
    print(display_horizontal(gmap, (24, 24, 0), 50))
    gmap = apply_automata(gmap, automaton_14_18)
    print(display_horizontal(gmap, (24, 24, 0), 50))
    gmap = apply_automata(gmap, automaton_14_18)
    print(display_horizontal(gmap, (24, 24, 0), 50))
        