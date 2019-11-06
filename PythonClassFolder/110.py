#!/usr/bin/python

#110
#Making A List

#Introduction: Lists, append(), Boolean

shoppingList = []
continueLooping = True

shoppingList.append(raw_input("What do you need to buy? >>>"))
while continueLooping == True:
	go = raw_input("Is that all you need? Type 'yes' or 'no'. >>>")
	if go == "yes":
		continueLooping = False
	elif go == "no":
		shoppingList.append(raw_input("What else do you need to buy? >>>"))
	else:
		print("Sorry, I didn't quite catch that.")

print("You need to buy:")
print(shoppingList)