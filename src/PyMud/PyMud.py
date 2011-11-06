'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import network.connection #@UnresolvedImport
import network.mudserver  #@UnresolvedImport
import command.command_handler #@UnresolvedImport


connection_data = {}
conn_fact = network.connection.ConnectionFactory(connection_data)

if __name__ == '__main__':
    server = network.mudserver.ConnectionServer('localhost', 8111, conn_fact)
    
    asyncore.loop()