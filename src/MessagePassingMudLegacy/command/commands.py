'''
Created on May 22, 2012

@author: Nich
'''

def say(p = None, args = None):
    if not args is None: 
        return ("You said: "+" ".join(args),)
    else:    
        return ("You open your mouth, but don't say anything",)

def dig(p = None, args = None):
    if len(args) is 2:
        dist = int(args[0])
        direction = args[1]
        act_dist = p.dig(dist, direction)
        return ("You dig "+str(act_dist)+" steps to the "+direction,)
    else:
        return ("Syntax is dig dist dir", \
                "where dist is a number indicating the number of steps to take", \
                "and dir is the direction to take them (n/s/e/w).")

def move(p = None, args = None):
    if len(args) is 2:
        dist = int(args[0])
        direction = args[1]
        act_dist = p.move(dist, direction)
        return ("You move "+str(act_dist)+" steps to the "+direction,)
    else:
        return ("Syntax is move dist dir", \
                "where dist is a number indicating the number of steps to take", \
                "and dir is the direction to take them (n/s/e/w).")
    

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