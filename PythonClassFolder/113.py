#!/usr/bin/python

#113
#Logic Gates

#Introduction: or, and, not

good = 0
print "OR"
while good == 0:
	num1 = int(input("Enter Two Numbers. One of them must be 2. >"))
	num2 = int(input(">"))
	if num1 == 2 or num2 == 2:
		good = 1
good = 0

print "AND"
while good == 0:
	num1 = int(input("Enter Two Numbers. Both of them must be 2. >"))
	num2 = int(input(">"))
	if num1 == 2 and num2 == 2:
		good = 1
good = 0

print "NOT"
while good == 0:
	num1 = int(input("Enter Two Numbers. The first number can not be 2. >"))
	num2 = int(input(">"))
	if not num1 == 2:
		good = 1