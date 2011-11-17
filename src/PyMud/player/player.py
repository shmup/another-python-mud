'''
Created on 2011-08-14

@author: Nich
'''
#TODO: make player persistent, secure password
#TODO: distinguish between password failed errors and username not found errors. Should the factory be enforcing that anyways?

class PlayerFactory(object):
    def __init__(self, player_store):
        self.player_store = player_store
    
    def getPlayer(self, username, password):
        if username in self.player_store:
            if self.player_store[username].password == password:
                return self.player_store[username]
            else:
                return None
    
    def hasPlayer(self, username):
        return username in self.player_store
        
    def buildNewPlayer(self, username, password, connection=None):
        if not username in self.player_store:
            player = TestPlayer(username, password, connection)
            self.player_store[username] = player
            return player
        else:
            return None
    
class TestPlayer(object):
    '''
    Provides storage of username and password and command handing functionality. Associated but distinct from a Character
    '''
    def __init__(self, username, password, connection = None):
        self.username = username
        self.password = password
        self.connection = connection
        
    def handle_command(self, command):
        print("This was called")
        self.connection.send(bytes(str(command)))
        
    def setConnection(self, conn):
        self.connection = conn
    
    def logged_in(self):
        return not self.connection is None