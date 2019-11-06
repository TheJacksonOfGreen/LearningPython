#!/usr/bin/python

#214
#Inheritance

#Introducing: [none]

class Dog():
	numberOfEars = 2
	breed = ""

class Beagle(Dog):
	breed = "Beagle"

	def __init__(self, name):
		name = self.name()

	def bark(self, thing):
		print self.name + " barked at " + thing + "!"

Instance = Beagle("Fido")

Instance.bark("the cat")
print Instance.name + " has " + Instance.numberOfEars + " ears."