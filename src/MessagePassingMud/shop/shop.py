'''
Created on Jun 15, 2012

@author: Nich
'''
from utils import coroutine
from command.command_matcher import match_command
from player.inventory import inv

sell_list = {'sell_list': {'sapphire':500,
                           'emerald':1000,
                           'ruby':5000,
                           'diamond':10000,
                           }}


def on_enter(prev_handler, p, conn):
    conn.push("shop", "open")
    _dest, msg = inv(p)
    conn.push("shop", msg)
    conn.push("shop", sell_list)
    conn.set_hander(sell_handler())
        
        
        
sell_commands = {"sell":{"function":sell, "num_args":2},
                 "quit":{"function":quit, "num_args":0},}        

@coroutine
def sell_handler(p, conn, matcher = match_command):
    while True:
        msg = yield conn.push("info", "To sell items, type 'sell # <item>', where # is the quantity you want to sell, and <item> is the name of the item. To exit, type 'quit'")
        command, args = matcher(p, msg, [sell_commands])
        result = command(p, args = args)
        for item in result:
            dest, msg = item
            conn.push(dest, msg)
            
def sell(p, args):
    qty = int(args[0])
    type = args[1]
    
    if type in sell_list["sell_list"]:
        p.add_money()
