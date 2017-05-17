#!/usr/bin/python

print "Content-type: text/html"
print

try:
	dataFile=open('165332CTF.txt', 'w')
	dataFile.close()
except IOError as err:
	print('FILE ERROR'+ str(err))	
