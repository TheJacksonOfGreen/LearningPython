#!/usr/bin/python

#209
#Testing Our Module

#Introduction: none

#IMPORTANT: Make sure to replace all instances of "CtoFModule" with whatever you named our last program. 

import CtoFModule

while True:
	choice = lower(raw_input("Convert Celsius to Farenheit or Farenheit to Celsius? >>>"))
	if choice == "celsius to farenheit":
		collect = float(raw_input("Enter a Number in degrees Celsius. >>>"))
		newValue = CtoFModule.CelsiusToFarenheit(collect)
		message = str(collect) + " degrees Celsius is equal to " + str(newValue) + " degrees Farenheit."
		print message
	if choice == "celsius to farenheit":
		collect = float(raw_input("Enter a Number in degrees Celsius. >>>"))
		newValue = CtoFModule.FarenheitToCelsius(collect)
		message = str(collect) + " degrees Celsius is equal to " + str(newValue) + " degrees Farenheit."
		print message