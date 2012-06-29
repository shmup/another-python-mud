'''
Created on Jun 28, 2012

@author: Nich
'''
from data.data_store import DataStore
from map.game_map import show_map

def show_map_callback():
    for p in DataStore.instance().data["all_players"]:
        conn = DataStore.instance().data["account_connection"][p.get_account()]
        for item in show_map(p):
            dest, msg = item
            if msg != {}:
                conn.push(dest, msg)