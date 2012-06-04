'''
Created on May 22, 2012

@author: Nich
'''

def say(p = None, args = None):
    if not args is None: 
        return ("You said: "+" ".join(args),)
    else:    
        return ("You open your mouth, but don't say anything",)

def goto(p = None, args = None):
    if not args is None:
        x, y, z = args
        x = int(x)
        y = int(y)
        z = int(z)
        if p.set_location((x, y, z)):
            return ("You move to " + str(p.get_location()),)
        else:
            return ("You can't move there, it is occupied",)
    else:
        return ("You need to enter an x, y and z coordinate",)
    
def n(p = None, args = None):
    loc = p.get_location()
    x, y, z = loc
    
    p.set_location((x, y+1, z))
    loc = p.get_location()
    return ("You move 1 step to the north (Your position is: "+str(loc)+")",)

def s(p = None, args = None):
    loc = p.get_location()
    x, y, z = loc
    p.set_location((x, y-1, z))
    loc = p.get_location()
    return ("You move 1 step to the south (Your position is: "+str(loc)+")",)

def e(p = None, args = None):
    loc = p.get_location()
    x, y, z = loc
    p.set_location((x+1, y, z))
    loc = p.get_location()
    return ("You move 1 step to the east (Your position is: "+str(loc)+")",)

def w(p = None, args = None):
    loc = p.get_location()
    x, y, z = loc
    p.set_location((x-1, y, z))
    loc = p.get_location()
    return ("You move 1 step to the west (Your position is: "+str(loc)+")", )