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

import math

def comparator(a, b):
	if math.sqrt(a[0]**2 + a[1]**2) > math.sqrt(b[0]**2 + b[1]**2):
		return 1
	elif  math.sqrt(a[0]**2 + a[1]**2) < math.sqrt(b[0]**2 + b[1]**2):
		return -1
	else:
		return 0
	
listaPTK = [(1, 4), (5, 9), (1, 5), (-4, 2), (2, 5)]
listaPTK2 = [(1, 4), (5, 9), (1, 5), (-4, 2), (2, 5)]

print("\nlista.sort")
listaPTK.sort()
print(listaPTK)


print("\nlista.sort(comparator)")
listaPTK2.sort(comparator)
print(listaPTK2)


print("\nsorted")
print(sorted(listaPTK))
print("\nsorted(comparator)")
print(sorted(listaPTK, comparator))


print("\nsorted z lambda")
lambdaComparator= lambda a,b:  int(math.sqrt(a[0]**2 + a[1]**2) - math.sqrt(b[0]**2 + b[1]**2))

listaPTK3 = [(1, 4), (5, 9), (1, 5), (-4, 2), (2, 5)]
print(listaPTK3)
print(sorted(listaPTK3,lambdaComparator))


######################################################################
print("\n\n")
#ZAD4

import os

print(os.listdir("."))
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		