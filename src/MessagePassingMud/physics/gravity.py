'''
Created on Jun 12, 2012

@author: Nich
'''
from player.player import get_all_players


def gravity(p):
    grav = p.get_effective_gravity()
    vel = p.get_velocity()+grav
    x, y, z = p.get_location()
    new_z = z + int(vel)
    p.set_location((x, y, new_z))
    
    
def gravity_callback():
    for p in get_all_players():
        gravity(p)