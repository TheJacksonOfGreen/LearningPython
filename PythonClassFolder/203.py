#!/usr/bin/python

#203
#The Urllib Module

#Introduction: urllib.urlopen, file.read, as

import urllib as url
#Using as in a program is optional.  It will still function the same if you get rid of "as url" and add lib after the first "url" in line 11 of this program.

file = url.urlopen('http://helloworldbook.com/data/message.txt')
#This is a program I got from the book I used to learn Python. 
#It's really the only simple example I could find for the urllib module, which is why the message will end up saying what it does.
message = file.read()
print message