'''
Created on Jun 4, 2012

@author: Nich
'''
def compose(*generators):
    while True:
        try:
            result = ""
            for g in generators:
                result += next(g)
            yield result 
        except StopIteration:
            raise StopIteration