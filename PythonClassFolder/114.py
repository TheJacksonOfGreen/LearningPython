#!/usr/bin/python

#114
#The For Loop

#Introduction: for, in

message = input("Let's say this letter by letter. >")
for letter in message:
	print letter
while True:
	number = input("Press enter to recieve 6 apples.")
	for looper in [1, 2, 3, 4, 5, 6]:
		print "You got an Apple!"
	number = input("Press enter to recieve 3 slices of watermelon.")
	for looper in [1, 6, 2]:
		print "You got a Slice of Watermelon!"
