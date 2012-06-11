'''
Created on Nov 27, 2011

@author: Nich
'''
from MessagePassingMud.network import connection_server
import asyncore


if __name__ == '__main__':
    server = connection_server.ConnectionServer('localhost', 8111)
    asyncore.loop() 