# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
t1=time.time()
def GetTime(fmt):
    loc1=time.localtime(t1)
    return time.strftime(fmt,loc1)

if __name__ == '__main__':
    print (GetTime("%Y-%m-%d"))
    print (GetTime("%Y-%m-%d %H:%M:%S"))
    print (GetTime("%Y-%m-%d %b %B %H:%M:%S %a %A"))