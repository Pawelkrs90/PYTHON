#!/usr/bin/env python

import sys

print(sys.argv[1:])
print(sys.argv[1])
a1 = int(sys.argv[1])
print(a1)


slownik = {}
slownik["k1"] = "v1"
slownik["k2"] = "v2"
slownik["k3"] = "v3"
slownik["k4"] = "v4"

print(slownik)

del slownik["k1"]

print(slownik)
print(slownik["k4"])
print(slownik["k4"]*2)
print(slownik.get("k8"))
print(slownik.get("k8", "Default Value"))

#iteracja po kluczach
for x in slownik:  
	print(x)

#iteracja po wartosciach	
for x in slownik.values():
	print(x)

#iteracja po kluczach i wartosciach
for x, y in slownik.items():
	print(x, y)
	
	

napis = "abc"
print(napis)
print('''linia1
linia2
linia3''')

napis = '.'.join(['a','b','c','d','e'])
print(napis)

napis = 'a b c'.split()
print(napis)

napis = "a,b,c,d,e,f".split(',')
print(napis)
	
	
lista1 = [1,2,3,4,5]
lista2 = [lista1]
print(lista1)

lista3 = lista2*3
print(lista3)

lista3[0][0] = "aaa"
print(lista3)
print(lista2)
print(lista1)

lista3 = [lista1[:]]*3
print(lista3)
lista3[0][0] = 3
print(lista3)






















#notepad++ /qq



