'''
Created on 2011-08-13

@author: Nich
'''

import asyncore
import socket
import collections


class CommandBuilder(object):
    @staticmethod
    def buildCommand(player, parser, message):
        context = Context(player, player.room, player.room.area, player.room.area.world)
        return Command(context, message[1], message[1:])

class CommandParser(asyncore.dispatcher_with_send):
    def __init__(self, handler, player, sock = None):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.handler = handler
        self.player = player
        
    def handle_read(self):
        data = self.recv(8192)
        if data:
            command = CommandBuilder.buildCommand(self.player, self, data.split())
            self.handler.addCommand(command)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port, handler, confactory):
        asyncore.dispatcher.__init__(self)
        self.handler = handler
        self.confactory = confactory
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        player = self.confactory.getPlayer(addr)
        CommandParser(self.handler, player, sock)


Command = collections.namedtuple("Command", ["context", "command", "args"])
Context = collections.namedtuple("CommandContext", ["player", "room", "area", "world"])