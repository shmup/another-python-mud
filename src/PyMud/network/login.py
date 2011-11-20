'''
Created on Nov 13, 2011

@author: Nich
'''


class LoginHandler(object):
    def __init__(self, next_handler, conn):
        self.conn = conn
        self.next = next_handler
        self.data = {}
        self.login_stack = [Login(self)]
        self.enter()
    def enter(self):
        self.login_stack[-1].enter()
    def handle_data(self, data):
        if not ("player" in self.data and self.data["player"].logged_in()):
            self.login_stack[-1].handle_data(data)
        else:
            self.next.handle_data(data)

    def hasPlayer(self, username):
        return self.conn.p_fact.hasPlayer(username)
    
    def getPlayer(self, username, password):
        return self.conn.p_fact.getPlayer(username, password)
    
    def buildNewPlayer(self, username, password):
        return self.conn.p_fact.buildNewPlayer(username, password, self.conn)
    
class MenuElement(object):
    def __init__(self, handler):
        self.data = handler.data
        self.conn = handler.conn
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
        if self.handler.hasPlayer(data): 
            self.handler.login_stack.append(Password(self.handler))
        else:
            self.handler.login_stack.append(Confirm(self.handler, GetPassword(self.handler)))
        self.handler.enter()
            
class Password(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
    
    def enter(self):    
        self.conn.send(b"Please enter your password")
        
    def handle_data(self, data):
        self.data["password"] = data
        p = self.handler.getPlayer(self.data["username"], self.data["password"])
        if not p:
            self.conn.send(b"Bad password")
        else:
            self.data["player"] = p
            self.handler.login_stack.append(Connect(self.handler))
        self.handler.enter()
        
class Confirm(MenuElement):
    def __init__(self, handler, next_step):
        MenuElement.__init__(self, handler)
        self.next = next_step

    def enter(self):
        self.conn.send(b"Account not found, do you want to create a new one with that name? (y/n)")
        
    def handle_data(self, data):
        print(data)
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
            self.data["player"] = self.handler.buildNewPlayer(self.data["username"], self.data["password"])
        self.handler.login_stack.append(Connect(self.handler))
        self.handler.enter()

class Connect(MenuElement):
    def __init__(self, handler):
        MenuElement.__init__(self, handler)
    
    def enter(self):
        self.data["player"].setConnection(self.conn)
        pass
            
    def handle_data(self, data):
        pass        
