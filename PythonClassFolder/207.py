#!/usr/bin/python

#207
#Calling A Variable from Inside a Function DONE RIGHT

#Introduction: global

x = 2

def divideByTwo(number):
	global x
	hello = number / x
	return hello

num = raw_input("Enter a Number. >")
total = divideByTwo(num)
print total
