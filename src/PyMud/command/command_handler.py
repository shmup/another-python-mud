'''
Created on 2011-08-13

@author: Nich
'''
import multiprocessing


class CommandHander(multiprocessing.Process):
    
    def __init__(self):
        multiprocessing.Process.__init__(self)
    
    def run(self):
        pass
                    