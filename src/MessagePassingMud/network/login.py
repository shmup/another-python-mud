'''
Created on Nov 27, 2011

@author: Nich
'''

from MessagePassingMud.model.account import make_account, get
from MessagePassingMud.player.player import get_default
from MessagePassingMud.utils.coroutine import coroutine
from MessagePassingMud.command.command_handler import json_command_handler

@coroutine
def handle_login(conn):
    while True:
        username = yield conn.push("Please enter your username")
        acc = get(username)
        if acc == None:
            answer = yield conn.push("Account not found, do you want to create one? (y/n)")
            if answer == "y":
                password = yield conn.push("Please enter your password")
                conf = yield conn.push("Please confirm your password")
                if password == conf:
                    make_account(username, password)
                    #Replace the below line with code to fetch the account's player
                    p = get_default()
                    conn.set_data_handler(json_command_handler(p, conn))
                    yield
                else:
                    conn.push("The passwords didn't match!")
            else:
                conn.push("Ok, bye")
        else:
            password = yield conn.push("Please enter your password")
            if acc.password == password:
                conn.push("Welcome!")
                #Replace the below line with code to fetch the account's player
                p = get_default()
                conn.set_data_handler(json_command_handler(p, conn))
                yield
            else:
                conn.push("Bad password")
                
'''
import time
@coroutine
def echo_handler(p, conn):
    import show_map
    while True:
        msg = yield
        s = show_map.show_map()
        for line in s:
            conn.push(bytes(line, 'utf-8'))
        conn.push(bytes(p.name+": "+msg, 'utf-8'))
        
'''
      
