'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import socket
import asynchat
import login #@UnresolvedImport

class DefaultHandler(object):
    def __init__(self, next_handler=None, connection=None):
        pass
    def handle_data(self, data):
        print("Mrrr, I'm the default handler I'm so cool")

handler_chain = [#login.LoginHandler, 
                 #AdminCommandHandler, 
                 #UserCommandHandler, 
                 DefaultHandler,
                 ]

def create_chain(command_stack, connection):
        if command_stack == []: return None
        last = command_stack[-1](None, connection)
        prev = None
        for i in range(2, len(command_stack)+1):
            prev = command_stack[-i](last, connection)
            last = prev
        return last



class ConnectionServer(asyncore.dispatcher):
    '''
    Spins up and handles the initial connection to the MUD
    '''
    def __init__(self, host, port, conn_factory, player_factory, command_handler):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.conn_factory = conn_factory
        self.player_factory = player_factory
        self.command_handler = command_handler

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        conn = CommandHandlerStack(sock, addr, self.player_factory)
        conn.setHandlers(create_chain(handler_chain, conn))
        
    def handle_error(self):
        raise
        
class CommandHandlerStack(asynchat.async_chat):
    def __init__(self, sock, addr, p_fact, c_fact = None, handlers = None):
        asynchat.async_chat.__init__(self, sock = sock)
        self.sock = sock
        self.addr = addr
        self.handlers = handlers
        self.p_fact = p_fact
        self.ibuffer = []
        self.obuffer = b""
        self.set_terminator(b"\n")
    
    def setHandlers(self, handlers):
        if self.handlers == None:
            self.handlers = handlers
        
    def collect_incoming_data(self, data):
        self.ibuffer.append(data)
    
    def found_terminator(self):
        data = b"".join(self.ibuffer)
        self.ibuffer = []
        split_data = data.splitlines()
        for d in split_data:
            d = str(d, "utf-8")
            self.handlers.handle_data(d)
       
            

'''
class ConnectionHandler(asynchat.async_chat):
    def __init__(self, sock, addr, handlers = None):
        
        self.handlers = handlers
        self.state = ""
        self.ibuffer = []
    
     
'''           