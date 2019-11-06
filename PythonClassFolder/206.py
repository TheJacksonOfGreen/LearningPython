#!/usr/bin/python

#206
#Calling A Variable from Inside a Function

#Introduction: none

x = 2

def divideByTwo(number):
	hello = number / x
	return hello

num = raw_input("Enter a Number. >")
total = divideByTwo(num)
print total