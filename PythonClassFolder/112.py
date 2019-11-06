#!/usr/bin/python

#112
#How to Break a loop

#Introduction: break

while True:
	ask = input("What should I say? Say 'Stop' if you want me to stop asking you. >")
	if ask == "Stop":
		break
	else:
		print(ask)
