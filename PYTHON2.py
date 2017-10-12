#!/usr/bin/env python

#slowniki itp

slownik = {}

slownik2 = {
	"klucz": "wartosc",
	"k2":"w2",
	"k3":"k3",
	"k4":"k5",
	4: "cztery",
	(1,2,3): "costam"
}

slownik["k0"] = "zerou"   #klucz o wartosci zero, wartosc "zero"
slownik["k1"] = 1
slownik[2] = 2

print(slownik)
print(slownik2)

slownik["k1"] = "nowa wartosc"

print(slownik)

print(slownik["k1"])

#print(slownik["k2"])  #nie ma takiego klucza - wyrzuca wyjatek KeyError

print(slownik.get("k2", "wartosc jesli brak klucza"))  #argument domyslny jest opcjonalny

#ITEROWANIE PO SLOWNIKU
for x in slownik:
	print(x)
	
for x, y in slownik.items():
	print(x, y)
	
	
##NAPISY

napis = "abc"
print(napis)
print('''napis linia1
linia2 eloe fdsfds''')

lista_napisow = ["dsfds", "fdsf", "gtgafg", "fffdf"]
wynik=''
for napis in lista_napisow:
	wynik+=napis
print(wynik)

zbitka = '.'.join(['a','b','c','d','e'])
print(zbitka)

rozwalka = 'a b c'.split()
print(rozwalka)

rozwalka = "a,b,c,d,e,f".split(',')
print(rozwalka)


#PLIKI
#f = open("plik.txt")
#print f.read()
#f.close()

#f = open("plik.txt")
#for line in f:
# print line
#f.close()

#with open("plik.txt") as f:
#  print f.read()
# tutaj plik jest już zamknięty

