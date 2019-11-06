#!/usr/bin/python

#202
#The Time Module

#Introduction: time.sleep

import time

Tminus = 10

while Tminus > 0:
	print Tminus
	time.sleep(1)
	Tminus -= 1
print "BLAST OFF!"