'''
Created on 2011-08-14

@author: Nich
'''

class PlayerFactory(object):
    @staticmethod
    def buildPlayer(player_id):
        player = TestPlayer(player_id)
        return player
    
class TestPlayer(object):
    '''
    Provides convenience methods to access the world
    '''
    
    def __init__(self, player_id, room=None):
        self.id = id
