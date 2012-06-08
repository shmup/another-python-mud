'''
Created on Nov 20, 2011

@author: Nich
'''
from coroutine import coroutine

#TODO: Player should be moved



@coroutine
def my_input(inbox):
    while True:
        message = (yield)
        sender = Player()
        local_area_targets = [Player(), Player(), Player()]
        args = message.split()
        inbox.send({"sender":sender, "targets":local_area_targets, "args":args})
        


class Player(object):
    def __init__(self):
        self.name = "Nich"
        
    
    '''@coroutine
    def output(self, inbox):
        while True:
            message = (yield)
            print(message["message"])
    '''
            
    def send(self, message):
        print(message)


