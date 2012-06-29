'''
Created on Jun 23, 2012

@author: Nich
'''

class GameMap(object):
    '''
    
    '''
    def __init__(self, gen = None, db = None, input_map = None):
        self.input_map = input_map
        self.db = db
    
    #def dig(self, loc):
        #return self.input_map[loc] if self.input_map and loc in self.input_map else 1
    
    def set(self, loc, val): #@ReservedAssignment
        if self.input_map:
            self.input_map[loc] = val
    
    def get(self, loc):
        return self.input_map[loc] if self.input_map and loc in self.input_map else 1
            
            
    def cache_next(self, loc, size):
        pass
    
