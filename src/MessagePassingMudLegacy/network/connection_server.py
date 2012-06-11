'''
Created on Nov 30, 2011

@author: Nich
'''
import asyncore
import socket
import asynchat
import MessagePassingMud.network.login as login

class ConnectionServer(asyncore.dispatcher):
    '''
    Spins up and handles the initial connection to the MUD
    '''
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        

    def handle_accepted(self, sock, addr):
        conn = ConnectionHandler(sock, addr)
        conn.set_data_handler(login.handle_login(conn))
        
    def handle_error(self):
        raise
    
class ConnectionHandler(asynchat.async_chat):
    def __init__(self, sock, addr, data_handler=None):
        asynchat.async_chat.__init__(self, sock = sock)
        self.sock = sock
        self.addr = addr
        self.ibuffer = []
        self.obuffer = b""
        self.set_terminator(b"\n")
        self.data_handler = data_handler
    
    def set_data_handler(self, data_handler):
        self.data_handler = data_handler
        
    def collect_incoming_data(self, data):
        self.ibuffer.append(data)
    
    def found_terminator(self):
        data = b"".join(self.ibuffer)
        self.ibuffer = []
        split_data = data.splitlines()
        for d in split_data:
            d_str = str(d, "utf-8")
            if not self.data_handler is None:
                self.data_handler.send(d_str)
            