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
    def __init__(self, host, port, conn_factory):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.conn_factory = conn_factory

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        self.conn_factory.register_connection(ConnectionHandler(sock, addr))
        

class ConnectionHandler(asynchat.async_chat):
    def __init__(self, sock, addr):
        asynchat.async_chat.__init__(self, sock=sock)
        self.addr = addr
        self.sock = sock
        self.set_terminator('/n')
    
    def handle_read(self):
        data = self.recv(8192)
        print(data)
        self.send(data)    