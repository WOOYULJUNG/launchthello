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

    mode = None

    # create an instance
    lp = launchpad.LaunchpadMk2()
    mode = "Mk2"
    lp.Open(0,"Mk2")

    # Clear the buffer because the Launchpad remembers everything :-)
    lp.ButtonFlush()
    lp.Reset()

    #lp.LedAllOn(1)
    while True:
            but = lp.ButtonStateXY()
            if but != []:
                print(" event: ", but )
                #lp.LedCtrlRaw( but[0], random.randint(0,63), random.randint(0,63), random.randint(0,63) )
                #lp.LedCtrlPulseByCode(but[0],random.randint(0,127))
                lp.LedCtrlXYByCode(but[0],but[1],8)
    #lp.LedSetLayout(00)
    # now quit...
    print("Quitting might raise a 'Bad Pointer' error (~almost~ nothing to worry about...:).\n\n")

    lp.Reset() # turn all LEDs off
    lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

    
if __name__ == '__main__':
    main()

