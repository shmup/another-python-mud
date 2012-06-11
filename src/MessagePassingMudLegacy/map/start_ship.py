'''
Created on Jun 10, 2012

@author: Nich
'''

def generate_starting_ship(pos):
    '''
    (o)/^\0[]S 
    #############
    ####(o)########
    ####/^\#######
    ###//0\\######
    ##// ^ \\#####       
    ##\\ ^ //####
    ##// ^ \\####
         ^   
    //[][S][]\\##
    #############
    '''
    base_dict = {(-1, -7):100, (0, -7):101, (1, -7):102,
                 (-1, -6):103, (0, -6):104, (1, -6):105,
                 (-2, -5):103, (-1, -5):103, (0, -5):106, (1, -5):105, (2, -5):105,
                 (-3, -4):103, (-2, -4):103, (-1, -4):110, (0, -4):104, (1, -4):110, (2, -4):105, (3, -4):105,
                 (-3, -3):105, (-2, -3):105, (-1, -3):110, (0, -3):104, (1, -3):110, (2, -3):103, (3, -3):103,
                 (-3, -2):103, (-2, -2):103, (-1, -2):110, (0, -2):104, (1, -2):110, (2, -2):105, (3, -2):105,
                 (-4, -1):110, (-3, -1):110, (-2, -1):110,(-1, -1):110, (0, -1):104, (1, -1):110, (2, -1):110, (3, -1):110, (4, -1):110,
                 (-5, 0):103, (-4, 0):103, (-3, 0):107, (-2, 0):108, (-1, 0):107, (0, 0):109, (1, 0):108, (2, 0):107, (3, 0):108, (4, 0):105, (5, 0):105}
    
    new_dict = {}
    for key in base_dict.keys():
        x, z = key
        px, py, pz = pos
        new_dict[(x + px, py, -(pz + z))] = base_dict[key]
        
    return new_dict
    
    