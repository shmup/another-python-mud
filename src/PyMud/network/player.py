'''
Created on 2011-08-14

@author: Nich
'''

class PlayerFactory(object):
    @staticmethod
    def buildPlayer(id):
        player = Player(id)
        return player
    
class Player(object):
    '''
    Provides convenience methods to access the world
    '''
    
    def __init__(self, id, room=None):
        self.id = id
