#!/usr/bin/python

#213
#__init__() functions

#Introducing: __init__

class Dog():
	breed = "Beagle"
	numberOfEars = 2

	def __init__(self, name):
		name = self.name()

	def bark(self, thing):
		print self.name + " barked at " + thing + "!"

Instance = Dog("Fido")

Instance.bark("the cat")