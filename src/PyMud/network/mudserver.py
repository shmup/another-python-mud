'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import socket
import asynchat


class ConnectionServer(asyncore.dispatcher):
    '''
    Spins up and handles the initial connection to the MUD
    '''
    def __init__(self, host, port, conn_factory, command_handler):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.conn_factory = conn_factory
        self.command_handler = command_handler

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        self.conn_factory.register_connection(ConnectionHandler(sock, addr, self.command_handler))
        

class ConnectionHandler(asynchat.async_chat):
    def __init__(self, sock, addr, handler = None):
        asynchat.async_chat.__init__(self, sock=sock)
        self.addr = addr
        self.sock = sock
        self.set_terminator('/n')
        self.handler = handler or None
    
    def handle_read(self):
        data = self.recv(8192)
        data = str(data, "utf-8")
        print(data)
        print("data passed to handler")
        self.handler.put(data.strip())
                