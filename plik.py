#!/usr/bin/env python

#PyQT

import json
import requests
import xml.etree.ElementTree as ET


#7/zad1
def getAddress(url, args):
	
	for key, value in args.items():
		url = url+'?'+key+'='+value
	
	return url
	
	
url = "https://www.youtube.com/watch"
args = {'v': 'dQw4w9WgXcQ', 'fullscreen': 'yes_or_no'}
print(getAddress(url, args))


#7/zad2
#def zad2():
#	try:
		#with open("plik.txt") as f:
		#	print(f.read())

#		f = open("plik.txt")	
#		print (f.read())

#		for line in f:
#			print(line)

#		f.close()
		
#except Exception:
#	print('read file error')

	

#7/zad3
def getSunrise(country, state, city):
	r = requests.get("http://www.yr.no/place/"+country+"/"+state+"/"+city+"/forecast.xml")
	#print(r.text)
	#print(r.headers['content-type'])
	doc = ET.fromstring(r.text)
	
	sunRise = doc.find("sun")
	#print(sunRise.tag)
	#print(sunRise.attrib['rise'])
	
	return sunRise.attrib['rise']

print("Lublin", getSunrise("Poland","Lublin","Lublin").split('T'))
print("Warszawa", getSunrise("Poland", "Masovia","Warsaw").split('T'))
	
	
#7/zad4
def getLatLang(city, street):
	r = requests.get("http://nominatim.openstreetmap.org/search/"+street+","+city+"?format=json")
	#print(r.text) 
	#print(r.json())
	jsonData = json.loads(r.text)
	
	for j in jsonData:
		print(j)
		
	#print(jsonData.lat)
	

	
getLatLang("Zana 12", "Lublin")
	
