#!/usr/bin/python

#212
#Functions within Classes

#Introducing: [none]

class Dog():
	name = "Fido"
	breed = "Beagle"
	numberOfEars = 2

	def bark(self, thing):
		print self.name + " barked at " + thing + "!"

Instance = Dog

Instance.bark("the cat")