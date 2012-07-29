'''
Created on Jun 28, 2012

@author: Nich
'''
from data.tiles import tiles, get_tile_property

def hit_test(old_loc, new_loc, game_map):
    tile_num = game_map.get(new_loc)
    return get_tile_property(tiles, tile_num, "walkable")



if __name__ == '__main__':
    pass