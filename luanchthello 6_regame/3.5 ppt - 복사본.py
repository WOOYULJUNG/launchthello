#!/usr/bin/env python
#
# Quick usage of "launchpad.py", LEDs and buttons.
# Works with all Launchpads: Mk1, Mk2, S/Mini, Pro, XL and LaunchKey
# 
#
# FMMT666(ASkr) 7/2013..2/2018
# www.askrprojects.net
#

import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

import random
from pygame import time


def main():

    ButtonColor = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    mode = None

    # create an instance
    lp = launchpad.LaunchpadMk2()
    mode = "Mk2"
    lp.Open(0,"Mk2")

    # Clear the buffer because the Launchpad remembers everything :-)
    lp.ButtonFlush()
    lp.Reset()
    while True:
            for i in range (0,99):
                if ButtonColor[i]==0:
                    lp.LedCtrlRawByCode(i,i)

    #lp.LedSetLayout(00)
    # now quit...
    print("Quitting might raise a 'Bad Pointer' error (~almost~ nothing to worry about...:).\n\n")

    lp.Reset() # turn all LEDs off
    lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

    
if __name__ == '__main__':
    main()

