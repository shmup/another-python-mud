'''
Created on Jun 4, 2012

@author: Nich
'''

dirs = {"n" : (0, 1, 0),
        "s" : (0, -1, 0),
        "e" : (1, 0, 0),
        "w" : (-1, 0, 0),}

def add_dirs(*dirs):
    res = [0, 0, 0]
    for d in dirs:
        for i, val in enumerate(d):
            res[i] = res[i]+val
    return tuple(res)