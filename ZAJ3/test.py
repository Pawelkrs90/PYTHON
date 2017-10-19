#!/usr/bin/env python

import datetime		
import time

liczby = range(-20, 20)
liczby_I_kwadraty = [(x, x**2) for x in liczby]
kwadraty_parzyste = [x**2 for x in liczby if x%2 == 0]
liczby_dodatnie = [x for x in liczby if x > 0]


print(liczby_I_kwadraty)
for x in range(-20, 20):
	print(x, x**2)


print(liczby_dodatnie)
for x in range(-20, 20):
	if x > 0:
		print(x)
		
		
print(kwadraty_parzyste)
for x in range(-20, 20):
	if x%2 == 0:
		print(x**2)

		
#LAMBDA
#kiedy uzywac - krotkie funkcje jedno linijkowe

kwadratX = lambda x : x**2
print("kwadrat 4: ", kwadratX(4))


lambdaAdd = lambda x,y: x+y
print("Wynik lambda plus ", lambdaAdd(4,6))


dataIgodzina = lambda: datetime.datetime.now().hour
print("Aktualna godzina: ",dataIgodzina())


#FUNKCJE WYRZSZEGO RZEDU


def gen_inc(n):
	def fun(x):
		return n+x
	return fun

inc5 = gen_inc(5)
print inc5(10)


def bankomat(x):
	return x

def posrednik(x):
	vat = 22
	return bankomat(x-(x/10))


print(bankomat(80))
print(posrednik(80))
	
	
def map(fun, list):
	return [fun(item) for item in list]

print map(lambda x: x+100, range(10))
	
#GENERATORY
	#umozliwia pobranie kolejnych elelemntow jakies sekwencji za pomoca next()
	
def generator(n):
	while n:
		print("zwracam %d z generatora." %n)
		yield n
		n-=1
		

#for x in generator(10):
 # time.sleep(0.5)
 # print('Wypisuje %d w petli.' % x)
 # time.sleep(0.5)		
		

######################################################################
print("\n\n")
#ZAD1#
napis = "dfsd df sdf sfdsf sdfds fstgrt fsdf h"
krotki = [(x, len(x)) for x in napis.split(" ")]
print(krotki)

######################################################################
print("\n\n")
#ZAD2#
def greaterThan10(x):
	return x>10

def equal66(x):
	return x == 66


def filter(condition, lista):
	lista2 = []
	
	for x in lista:
		if condition(x):
			lista2.append(x)
	
	return lista2
	
	
list = [1, 3, 55, 66, 3, 12, 444, 22,66, 9, 8, 23]
list2 = filter(greaterThan10, list)
print(list2)
list3 = filter(equal66, list)
print(list3)

######################################################################
print("\n\n")
#ZAD3#

def punkty(lista)
	

	
	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		