#!/usr/bin/env python

import math

def rzymska(liczba):
	
	if liczba>3999:
		raise ValueError("Value is out of range") 
		
	tysiace = math.trunc(liczba/1000)	
	setki = math.trunc((liczba - tysiace*1000)/100)
	dziesiatki = math.trunc((liczba - tysiace*1000 - setki*100)/10)
	jednostki = liczba-(tysiace*1000)-(setki*100)-(dziesiatki*10)

	rzymska = ""
	rzymska = liczTysiace(tysiace, rzymska)
	rzymska = liczSetki(setki, rzymska)
	rzymska = liczDzisiatki(dziesiatki, rzymska)
	rzymska = liczJednostki(jednostki, rzymska)

	return rzymska

	
def liczTysiace(tysiace, rzymska):
	
	if tysiace>0 :  # tys
		rzymska = "M"*tysiace
	
	return rzymska

def liczSetki(setki, rzymska):
	
	if setki>0 :

		if setki == 9:
			rzymska += "CM"
		elif setki >= 5:
			rzymska += "D"
			rzymska += (setki-5)*"C"	
		elif setki == 4:
			rzymska += "CD"
		else:
			rzymska += setki*"C"
	
	return rzymska

def liczDzisiatki(dziesiatki, rzymska):

	if dziesiatki == 9:
		rzymska += "XC"
	elif dziesiatki >= 5:
		rzymska += "L"
		rzymska += (dziesiatki-5)*"X"
	elif dziesiatki == 4:
		rzymska += "XL"
	else:
		rzymska += dziesiatki*"X"	

	return rzymska

def liczJednostki(jednostki, rzymska):

	if jednostki == 9:
		rzymska += "IX"
	elif jednostki >=5 :
		rzymska += "V"
		rzymska += (jednostki-5)*"I"
	elif jednostki == 4:
		rzymska +="IV"
	else:
		rzymska += jednostki*"I"

	return rzymska


try:
	print("3999", rzymska(3999))
	print(rzymska(4000))
except ValueError, e:
	print("Uwaga", e)












































#https://docs.djangoproject.com/en/1.11/topics/db/models/
#http://www.effectivedjango.com/tutorial/models.html
#https://tutorial.djangogirls.org/pl/django_models/
#
#
#
#

