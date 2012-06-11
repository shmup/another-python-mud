'''
Created on Jun 4, 2012

@author: Nich
'''
def compose(*generators, separator = ""):
    while True:
        try:
            result = ""
            for g in generators:
                result += next(g) + separator
            yield result[:-len(separator)] 
        except StopIteration:
            raise StopIteration