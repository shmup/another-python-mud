'''
Created on Nov 27, 2011

@author: Nich
'''

from model.account import make_account, get
from utils.coroutine import coroutine
from command.command_handler import command_handler
from data.data_store import DataStore

@coroutine
def handle_login(conn):
    while True:
        username = yield conn.push("login", "Please enter your username")
        acc = get(username)
        if acc == None:
            answer = yield conn.push("login", "Account not found, do you want to create one? (y/n)")
            if answer == "y":
                password = yield conn.push("login", "Please enter your password")
                conf = yield conn.push("login", "Please confirm your password")
                if password == conf:
                    account = make_account(username, password)
                    #Replace the below line with code to fetch the account's player
                    p = DataStore.instance().data["default_player"]
                    DataStore.instance().add_player(p)
                    p.set_account(account)
                    DataStore.instance().data["account_connection"][account] = conn
                    conn.set_data_handler(command_handler(p, conn))
                    yield
                else:
                    conn.push("login", "The passwords didn't match!")
            else:
                conn.push("login", "Ok, bye")
        else:
            password = yield conn.push("login", "Please enter your password")
            if acc.password == password:
                conn.push("login", "Welcome!")
                #Replace the below line with code to fetch the account's player
                DataStore.instance().data["account_connection"][acc] = conn
                p = DataStore.instance().data["default_player"]
                DataStore.instance().add_player(p)
                p.set_account(acc)
                conn.set_data_handler(command_handler(p, conn))
                yield
            else:
                conn.push("login", "Bad password")
                

      
