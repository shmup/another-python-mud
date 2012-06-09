'''
Created on Jun 4, 2012

@author: Nich
'''

import random
mult = 1111
const = 125
#3677   3691   3697



def generate(odds, i, j, k, offset):
    seed = str(i)+str(j)+str(k)+str(offset)
    random.seed(seed)
    number = random.randint(1, odds)
    return 1 if number == 1 else 0

def generate_terrain(i, j, k):
    kpart = ((k*mult + const) % 3676)
    jpart = ((j*kpart + const) % 3691)
    ipart = ((i*jpart + const) % 3697)
     
    val = (ipart ^ jpart ^ kpart) %2
    return val

def generate_gemstone(i, j, k):
    sapp = 2 if generate(100, i, j, k, 0) == 1 else 0
    em = 3 if generate(100, i, j, k, 50) == 1 else 0
    
    return sapp or em or 0 


def generate_tile(i, j, k):
    gem = generate_gemstone(i, j, k) 
    if gem >= 2:
        return gem
    return generate_terrain(i, j, k) 


if __name__ == "__main__":
    k = 0
    for j in range(100):
        line = ""
        for i in range(100):
            line += str(generate_gemstone(i, j, k))
        print(line)

