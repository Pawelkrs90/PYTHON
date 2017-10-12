#!/usr/bin/env python

#import sys
#print(sys.argv)

#nazwaPliku = sys.argv[1]
#klucz = sys.argv[2]

def mySplit(napis):
	lista = napis.split('\n')
	slownik={}
	for x in lista[0:len(lista)-1]:
		L = x.split(':')
		slownik[L[0]] = L[1]
		
	return slownik

#f = open("/home/student/pythonPlik.txt")
#textZPliku =  f.read()
#f.close()

with open("/home/student/pythonPlik.txt") as f:
	textZPliku =  f.read()

#print(textZPliku)
#Lista = textZPliku.split('\n')
#print(Lista)

slownik = mySplit(textZPliku)
print(slownik)