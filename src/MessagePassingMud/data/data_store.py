'''
Created on Jun 14, 2012

@author: Nich
'''

class DataStore(object):
    '''
    classdocs
    '''


    def __init__(self):
        self._data = {}
    
    
    def add_player(self, p):
        if not p in self._data["all_players"]:
            self._data["all_players"].append(p)
    
    @property
    def data(self):
        return self._data
    
    @staticmethod
    def instance():
        if not hasattr(DataStore, "_instance"):
            DataStore._instance = DataStore()
        return DataStore._instance    