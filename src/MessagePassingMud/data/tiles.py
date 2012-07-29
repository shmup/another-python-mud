'''
Created on Jun 28, 2012

@author: Nich
'''

def pickup(tile_num, p):
    p.inventory.append(tile_num)

tiles = {
         "default": {"name":"default",
             "density":float("inf"),
             "walkable":False,
             "on_enter":None,
             "on_exit":None,
             "tile_commands":{}},
         0: {"name":"empty",
             "density":0,
             "walkable":True},
         1: {"name":"soil",
             "density":0,
             "walkable":False},
         2: {"name":"sapphire",
             "on_enter":pickup},
         3: {"name":"emerald",
             "on_enter":pickup},
         4: {"name":"ruby",
             "on_enter":pickup},
         5: {"name":"diamond",
             "on_enter":pickup},
         9: {"name":"iron",
             "on_enter":pickup},
         }

def get_tile_property(tile_dict, tile_num, tile_property):
    if tile_num in tile_dict:
        if tile_property in tile_dict[tile_num]:
            return tiles[tile_num][tile_property]
    return tile_dict["default"][tile_property]    
    

    
    

    