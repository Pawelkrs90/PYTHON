#!/usr/bin/env python

#import sys
#print(sys.argv)

def mySplit(napis):
	lista = napis.split('\n')
	slownik={}
	for x in lista:
		L = x.split(':')
		slownik[L[0]] = L[1]
		
	return slownik
	
slownik = mySplit('''k1:v1
k2:v2
k3:v3
k4:v4
k5:v5''')

for x, y in slownik.items():
	print(x, y)
	
	
print(slownik)
	