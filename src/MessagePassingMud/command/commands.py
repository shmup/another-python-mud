'''
Created on May 22, 2012

@author: Nich
'''
#from map.game_map import show_map



def say(p = None, args = None):
    if not args is None: 
        return ("info", "You said: "+" ".join(args)),
    else:    
        return ("info", "You open your mouth, but don't say anything"),

def dig(p = None, args = None):
    if len(args) is 1:
        direction = args[0]
        act_dist = p.dig(direction)
        return ("info", "You dig "+str(act_dist)+" steps to the "+direction),
    else:
        return (("info", "Syntax is dig dist dir"), 
                ("info", "where dist is a number indicating the number of steps to take"), 
                ("info", "and dir is the direction to take them (n/s/e/w)."))

def move(p = None, args = None):
    if len(args) is 1:
        direction = args[0]
        act_dist = p.move(direction)
        return ("info", "You move "+str(act_dist)+" steps to the "+direction),
    else:
        return (("info", "Syntax is dig dist dir"), 
                ("info", "where dist is a number indicating the number of steps to take"), 
                ("info", "and dir is the direction to take them (n/s/e/w)."))
    

def goto(p = None, args = None):
    if not args is None:
        x, y = args
        x = int(x)
        y = int(y)

        p.set_location((x, y))
        return ("info", "You move to " + str(p.get_location())),
    else:
        return ("info", "You need to enter an x, y coordinate"),
    


