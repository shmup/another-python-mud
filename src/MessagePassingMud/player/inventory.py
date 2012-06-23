'''
Created on Jun 14, 2012

@author: Nich
'''

from data.data_store import DataStore

def inv(p, args = None):
    new_dict = {}
    inv = p.get_inventory()
    num_sapp = inv.count(2)
    num_em = inv.count(3)
    num_rub = inv.count(4)
    num_diam = inv.count(5)
    if num_sapp > 0:
        new_dict["sapphire"] = num_sapp
    if num_em > 0:
        new_dict["emerald"] = num_em
    if num_rub > 0:
        new_dict["ruby"] = num_rub
    if num_diam > 0:
        new_dict["diamond"] = num_diam
    return ("inv", new_dict)

def inventory_callback():
    for p in DataStore.instance().data["all_players"]:
        conn = DataStore.instance().data["account_connection"][p.get_account()]
        dest, msg = inv(p)
        conn.push(dest, msg)
        