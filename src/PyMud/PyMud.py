'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import network.connection #@UnresolvedImport
import network.mudserver  #@UnresolvedImport
import command.command_handler #@UnresolvedImport
import player.player #@UnresolvedImport
import logging, multiprocessing
logger = multiprocessing.log_to_stderr(logging.INFO)

player_data = {}
player_fact = player.player.PlayerFactory(player_data)

connection_data = {}
conn_fact = network.connection.ConnectionFactory(connection_data, player_fact)
comm_queue = multiprocessing.Queue()
ch = command.command_handler.StringCommandHandler(comm_queue)
comm_process = command.command_handler.CommandProcess(comm_queue)

if __name__ == '__main__':
    try:
        server = network.mudserver.ConnectionServer('localhost', 8111, conn_fact, ch)
        comm_process.daemon = True
        comm_process.start()
        asyncore.loop()
    finally:
        comm_queue.put("exit", True, None)
        asyncore.close_all()
        
