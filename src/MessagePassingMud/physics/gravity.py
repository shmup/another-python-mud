'''
Created on Jun 12, 2012

@author: Nich
'''
from data.data_store import DataStore


def gravity(p):
    grav = p.get_effective_gravity()
    vel = p.get_velocity()+grav
    x, y = p.get_location()
    new_y = y + int(vel)
    p.set_location((x, new_y))
    
    
def gravity_callback():
    for p in DataStore.instance().data["all_players"]:
        gravity(p)