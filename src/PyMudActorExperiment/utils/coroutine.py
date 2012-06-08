'''
Created on Nov 19, 2011

@author: Nich
'''
def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start