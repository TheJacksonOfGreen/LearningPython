#!/usr/bin/python

#208
#Functions with Multiple Inputs and Outputs

#Introduction: [none]

def changeNumbers(number1, number2):
	number1 += 5
	number2 -= 7
	return number1, number2

numA = int(raw_input("Enter a Number. >"))
numB = int(raw_input("Enter Another Number. >"))
numA, numB = changeNumbers(numA, numB)
print numA
print numB