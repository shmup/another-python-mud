'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import network.connection #@UnresolvedImport
import network.mudserver  #@UnresolvedImport
import command.command_handler #@UnresolvedImport
import player.player #@UnresolvedImport



player_data = {}
player_fact = player.player.PlayerFactory(player_data)
ch = command.command_handler.CommandHandler()
connection_data = {}
conn_fact = network.connection.ConnectionFactory(connection_data, ch, player_fact)



if __name__ == '__main__':
    server = network.mudserver.ConnectionServer('localhost', 8111, conn_fact)
    ch.start()
    asyncore.loop()