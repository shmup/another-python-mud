'''
Created on Jun 18, 2012

@author: Nich
'''

def gen_tile(x, y):
    return 1


def gen_sec(sector, size):
    sec_x, sec_y = sector
    x_size, y_size = size
    x_min, x_max = sec_x*x_size, sec_x*x_size+x_size
    y_min, y_max = sec_y*y_size, sec_y*y_size+y_size
    
    sector_map = {}
    for ny in range(y_min, y_max):
        for nx in range(x_min, x_max):
            nloc = (nx, ny)
            sector_map[nloc] = 1
    
    return sector_map