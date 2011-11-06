'''
Created on Nov 4, 2011

@author: Nich
'''

class ConnectionFactory(object):
    def __init__(self, connection_store):
        self.connection_store = connection_store
        self.current_id = 0
    
    def register_connection(self, handler):
        conn = Connection(handler)
        self.connection_store[self.get_id()] = conn
    
    def deregister_connection(self, id):
        del self.connection_store[id]
    
    def get_id(self):
        self.current_id += 1
        return self.current_id-1


class Connection(object):
    '''
    classdocs
    '''
    def __init__(self, handler):
        self.addr = handler.addr
        self.sock = handler.sock
        self.handler = handler
        
    def send(self, message):
        self.hander.send(message)
        
    
        