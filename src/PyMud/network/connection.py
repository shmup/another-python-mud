'''
Created on Nov 4, 2011

@author: Nich
'''

class ConnectionFactory(object):
    def __init__(self, connection_store, command_handler, player_factory):
        self.connection_store = connection_store
        self.command_handler = command_handler
        self.player_factory = player_factory
        self.current_id = 0
    
    def register_connection(self, handler):
        c_id = self.get_id()
        conn = Connection(c_id, handler, self.command_handler, self.player_factory)
        self.connection_store[c_id] = conn
        return conn
    
    def deregister_connection(self, conn_id):
        del self.connection_store[conn_id]
    
    def get_by_id(self, c_id):
        if c_id in self.connection_store:
            return self.connection_store[c_id]
        else:
            return None    
    
    def get_id(self):
        self.current_id += 1
        return self.current_id-1


class Connection(object):
    '''
    classdocs
    '''
    def __init__(self, c_id, handler, command_handler, player_fact):
        self.c_id = c_id
        self.addr = handler.addr
        self.sock = handler.sock
        self.handler = handler
        self.command_handler = command_handler
        self.player_fact = player_fact
        
    def send(self, message):
        self.handler.send(message)
        
    
        