'''
Created on Jun 28, 2012

@author: Nich
'''
from data.tiles import tiles

def hit_test(old_loc, new_loc, game_map):
    tile_num = game_map.get(new_loc)
    if tile_num in tiles:
        return tiles[tile_num]["walkable"]
    else:
        return False



if __name__ == '__main__':
    pass