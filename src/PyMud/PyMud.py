'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import network.connection #@UnresolvedImport
import network.mudserver  #@UnresolvedImport
import command.command_handler #@UnresolvedImport
import player.player #@UnresolvedImport
from multiprocessing import Queue



player_data = {}
player_fact = player.player.PlayerFactory(player_data)

connection_data = {}
conn_fact = network.connection.ConnectionFactory(connection_data, player_fact)
comm_queue = Queue()
ch = command.command_handler.StringCommandHandler(comm_queue)
comm_process = command.command_handler.CommandProcess(comm_queue)

if __name__ == '__main__':
    server = network.mudserver.ConnectionServer('localhost', 8111, conn_fact, ch)
    comm_process.start()
    asyncore.loop() 