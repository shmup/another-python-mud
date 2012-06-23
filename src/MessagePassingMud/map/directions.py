'''
Created on Jun 4, 2012

@author: Nich
'''

dirs = {
        "e" : (1, 0),
        "w" : (-1, 0),
        "d" : (0, -1),
        }

def add_dirs(*dirs):
    res = [0, 0]
    for d in dirs:
        for i, val in enumerate(d):
            res[i] = res[i]+val
    return tuple(res)