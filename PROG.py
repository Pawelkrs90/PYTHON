#!/usr/bin/env python

print("Hello word yol")

#Import

import math
print(math.sqrt(25))
print(math.pow(5,2))

#: math. 
#math.acos       math.atanh      math.e          math.factoria
#l  math.hypot      math.log10      math.sin 
#math.acosh      math.ceil       math.erf        math.floor   
#  math.isinf      math.log1p      math.sinh 
#math.asin       math.copysign   math.erfc       math.fmod    
#  math.isnan      math.modf       math.sqrt 
#math.asinh      math.cos        math.exp        math.frexp   
#  math.ldexp      math.pi         math.tan 
#math.atan       math.cosh       math.expm1      math.fsum    
#  math.lgamma     math.pow        math.tanh 
#math.atan2      math.degrees    math.fabs       math.gamma   
#  math.log        math.radians    math.trunc 

#ZMIENNE

intek = 5
stringus = "tekst"
charek = 'H'
zmienny = 8.8
logic = True

print("ZMIENNE:",intek, stringus, charek, zmienny)
#Printfowanie %.2f, %.2f' % x1, x

#ARYTMETYKA

print(5+intek)
intek = 2*intek
print(intek)
print(stringus+" i doklejony tekst")
#standardowe operatory



#IF
logic = -logic   # ! iedziala  '-' oznacza przeciwna wartosc

if logic == True:
	print("dziala, jest true")
elif intek % 2 == 1:
	print("nie true i intek nieparzysty")
else:	
	print("nie true i intek parzysty")
	
#LISTY
auta = ["Opel", "Mazda", "BMW", "Audi"]	
print(auta)
auta.extend(["Toyota", "VW"])
print(auta)
print(auta[:])
print(auta[0:3])   #od 0 do 3 (bez 3)
print(auta[3:])	   #od 3 wlacznie do konca
	
auta.append(["Fiat", "Skoda"])
print(auta)

print("Size of list",len(auta))   #size of list

lista = []
if lista: 
    print('lista jest niepusta')
else: 
    print('lista jest pusta')

for x in lista: 
    print(x, x*x)
	
#Krotki  (w krotkach moga byc elementy roznuch typow)
krotka = (18, "pawel", ["mazda", "opel"], 724601982)
print(krotka)

#kopiowanie listy
auta2 = auta   #to nie jest kopiowanie tylko powielenie wskaznika na liste
auta3 = auta[:] #to jest przekopiowanie calej listy

#PETLE
#FOR
print("FOR")
for x in range(10):
	print(x)
	
for x in "Python":
	print(x, end='') # end=''  znak miedzy znakami
	
for x in "Python":
	print(x, end=' ')    

Lista = [1,2,3,4,5,6]	
for item in Lista:
	print(item)

print()
	
for x in range(1, 11):
	print(x, end='')
	
#WHILE
print()
print("WHILE")
i = 0
while i<10:
	print(i)
	i+=1
	
#FUNKCJE
def get8():
	return 8

def suma(a, b):
	return a+b
	
def sayHello():
	print("Hello")
	
print("Suma:", suma(5, 10))
sayHello()

print(suma(3, .14159265897))
	
def fibo(n): 
    a, b = 0, 1 
    while n: 
        n -= 1 
        a, b = b, a+b 
    return a 
	
def rozwiazania_trojmianu(a,b,c): 
       delta = b*b-4.0*a*c 
       if delta < 0.0: 
           return [] 
       elif delta == 0.0: 
           return [-b/(2.0*a)] 
       else: 
           return [  (-b-math.sqrt(delta))/(2.0*a), 
                     (-b+math.sqrt(delta))/(2.0*a), 
                  ] 
#---------------------------------------------------------------#
#klasy

	
	

	
