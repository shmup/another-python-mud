'''
Created on Jun 12, 2012

@author: Nich
'''
from data.data_store import DataStore


def gravity(p):
    p.move("d")
    
    
def gravity_callback():
    for p in DataStore.instance().data["all_players"]:
        gravity(p)