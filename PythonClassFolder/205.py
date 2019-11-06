#!/usr/bin/python

#205
#Taking Parameters

#Introduction: def myFunction(x), return x

def Add(number1, number2):
	total = number1 + number2
	return total

single = int(raw_input("Enter A Number. >"))
double = int(raw_input("Enter Another Number. >"))
composite = Add(single, double)
print "The total is " + str(composite)