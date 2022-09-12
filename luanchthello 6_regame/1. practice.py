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


	# scroll "HELLO" from right to left
	lp.LedCtrlString( "HELLO ", 0, 63, 0, -1 )


	# random output
	if mode == "LKM":
		print("The LaunchKey(Mini) does not (yet) support LED activation, but you")
		print("can push some buttons or rotate some knobes now...")
		print("Auto exit if first number reaches 0")
	else:
		print("---\nRandom madness. Create some events. Stops after reaching 0 (first number)")
		print("Notice that sometimes, old Mk1 units don't recognize any button")
		print("events before you press one of the (top) automap buttons")
		print("(or power-cycle the unit...).")

	# Clear the buffer because the Launchpad remembers everything :-)
	lp.ButtonFlush()

	# Lightshow
	butHit = 10
		
	while 1:
		lp.LedCtrlRaw( random.randint(0,127), random.randint(0,63), random.randint(0,63), random.randint(0,63) )
		time.wait( 5 )

		but = lp.ButtonStateRaw()
		print(butHit)

		if but != []:
			butHit -= 1
			if butHit < 1:
				break
			print( butHit, " event: ", but )

	# now quit...
	print("Quitting might raise a 'Bad Pointer' error (~almost~ nothing to worry about...:).\n\n")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

