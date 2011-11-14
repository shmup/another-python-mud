'''
Created on Nov 13, 2011

@author: Nich
'''
import asyncore, socket, asynchat
from connection import ConnectionFactory
from player.player import PlayerFactory
from mudserver import ConnectionHandler

class LoginHandlerConnection(asynchat.async_chat):
    def __init__(self, sock, addr, conn_fact, player_fact, command_handler):
        asynchat.async_chat.__init__(self, sock=sock)
        self.addr = addr
        self.sock = sock
        self.set_terminator('/n')
        self.conn_fact = conn_fact
        self.player_fact = player_fact
        self.command_handler = command_handler
        self.login = LoginHandler(self, self.player_fact)
        
        
    def handle_read(self):
        data = self.recv(8192)
        self.login.handle_data(data)
    
    
    
class LoginHandler(object):
    
    def __init__(self, connection, player_fact):
        self.connection = connection
        self.data = {}
        self.player_factory = player_fact
        self.login_stack = [Login(self)]
        self.enter()
    
    def enter(self):
        self.login_stack[-1].enter()
    
    def handle_data(self, data):
        data = str(data, "utf-8").strip()
        self.login_stack[-1].handle_data(data)
    
class MenuElement(object):
    def __init__(self, handler):
        self.data = handler.data
        self.p_fact = handler.player_factory
        self.conn = handler.connection
        self.handler = handler
    def enter(self):
        pass
    def handle_data(self, data):
        pass
        
class Login(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
        
    def enter(self):
        self.conn.send(b"Please enter your username")    
        
    def handle_data(self, data):
        self.data["username"] = data
        if self.p_fact.hasPlayer(data): 
            self.handler.login_stack.append(Password(self.handler))
        else:
            self.handler.login_stack.append(Confirm(self.handler, GetPassword(self.handler)))
        self.handler.enter()
            
class Password(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
    
    def enter(self):    
        self.conn.send(b"Please enter your password/n")
        
    def handle_data(self, data):
        self.data["password"] = data
        p = self.getPlayer(self.data["username"], self.data["password"])
        if not p:
            self.conn.send(b"Bad password")
        else:
            #We should be fine to launch into the actual connection
            pass 
        self.handler.enter()
        
class Confirm(MenuElement):
    def __init__(self, handler, next_step):
        MenuElement.__init__(self, handler)
        self.next = next_step

    def enter(self):
        self.conn.send(b"Account not found, do you want to create a new one with that name? (y/n)")
        
    def handle_data(self, data):
        if data == "y": 
            self.handler.login_stack.append(self.next)
        elif data == "n":
            self.handler.login_stack.pop()
        self.handler.enter()

    
class GetPassword(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
        
    def enter(self):
        self.conn.send(b"Please enter a password: ")    
        
    def handle_data(self, data):
        self.data["password"] = data
        self.handler.login_stack.append(ConfirmPassword(self.handler))
        self.handler.enter()
        

class ConfirmPassword(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
    
    def enter(self):
        self.conn.send(b"Please confirm your password: ")
    
    def handle_data(self, data):
        self.data["cpassword"] = data
        
        if self.data["password"] == self.data["cpassword"]:
            self.data["player"] = self.p_fact.newBuildPlayer(self.data["username"], self.data["password"])
        self.handler.login_stack.append(Connect(self.handler))
        self.handler.enter()

class Connect(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
    
    def enter(self):
        conn = ConnectionHandler(self.handler.connection.sock, self.handler.connection.addr, self.handler.connection.command_handler)
        self.handler.connection.conn_fact.register_connection(conn)
        self.data["player"].setConnection(conn)
            
    
    def handle_data(self, data):
        pass        
