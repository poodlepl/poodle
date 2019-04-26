from modules.parser import *


def icg():
    # get all these variables somehow.
    global cond, left_val, right_val
    c, l, r = while_()

    print("I am in icg. Values are: " +str(c) +str(l) +str(r))

    print('L1: if %s not %s %s goto L3' % (left_val, cond, right_val))
    
