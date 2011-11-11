'''
Created on 2011-08-14

@author: Nich
'''
#TODO: make player persistent, secure password


class PlayerFactory(object):
    def __init__(self, player_store):
        self.player_store = player_store
    
    def getPlayer(self, username, password):
        if username in self.player_store:
            if self.player_store[username].password == password:
                return self.player_store[username]
            else:
                return None
        
    def newBuildPlayer(self, username, password):
        if not username in self.player_store:
            player = TestPlayer(username, password)
            self.player_store[username] = player
            return player
        else:
            return None
    
class TestPlayer(object):
    '''
    Provides storage of username and password and command handing functionality. Associated but distinct from a Character
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def handle_command(self, command, connection):
        pass