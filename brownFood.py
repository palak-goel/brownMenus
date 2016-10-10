import requests
from bs4 import BeautifulSoup
import re

def getToRattyMenu():

	f_r = requests.get('http://brown.cafebonappetit.com/cafe/sharpe-refectory/2016-10-11/')
	f_soup = BeautifulSoup(f_r.content,'html.parser')

	a = f_soup.find('article', class_ = 'cafe-daypart-panel nav-storage')
	a = str(a)
	b = a.split('day')
	c = b[6]
	d = c[3:]
	return d

def removeTags(listy):
    cleanList = []
    for item in listy:
        cleanList.append(re.sub('<\S+>|</\S+>', '', str(item)))
    return cleanList 

def cleanEscapeCharacters(stringy):
    return stringy.replace('\\', '')

print cleanEscapeCharacters(str(getToRattyMenu()))

r = requests.get(cleanEscapeCharacters(str(getToRattyMenu())))
soup = BeautifulSoup(r.content,"html.parser")

'''
breakfast = soup.find('div', {'class':'fulldaymenu'})
lunch = breakfast.find('div', {'class':'fulldaymenu'})
dinner = lunch.find('div', {'class':'fulldaymenu'})
dinner_items = dinner.find_all('strong')
lunch_items = filter(lambda x: x not in dinner_items, lunch.find_all('strong'))
breakfast_items = filter(lambda x: x not in lunch_items and x not in dinner_items, breakfast.find_all('strong'))

print (removeTags(dinner_items))
#print removeTags(lunch_items)
#print removeTags(breakfast_items)
'''


