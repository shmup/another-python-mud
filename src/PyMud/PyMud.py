'''
Created on 2011-08-14

@author: Nich
'''
import asyncore
import network.mudserver


if __name__ == '__main__':
    server = network.mudserver.ConnectionServer('localhost', 8111)
    asyncore.loop()