#!/usr/bin/python

#201
#Importing a Module

#Introduction: import, sys.exit

import sys

while True:
	closing = raw_input("To close this program, type a single Uppercase X. >")
	if closing == "X":
		sys.exit()
	else:
		print "Okay! I'll keep running!"