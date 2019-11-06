#!/usr/bin/python

#210
#The Lambda Function

#Introduction: lambda

r = lambda x, y: x * y

print str(r(5, 6))

def createAMultiplier(n):
	return lambda a: a * n

myDoubler = createAMultiplier(2)
myTripler = createAMultiplier(3)

print myDoubler(11)
print myTripler(11)