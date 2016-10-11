import requests
from bs4 import BeautifulSoup
import re

def get_to_menu(eatery):
	f_r = requests.get('http://brown.cafebonappetit.com/cafe/' + eatery + '/2016-10-11/')
	f_soup = BeautifulSoup(f_r.content,'html.parser')

	a = f_soup.find('article', class_ = 'cafe-daypart-panel nav-storage')
	a = str(a)
	b = a.split('day')
	c = b[6]
	d = c[3:]
	return d

def remove_tags_and_encodings(listy):
    cleanList = []
    for item in listy:
        item = re.sub('<\S+>|</\S+>', '', str(item))
        cleanList.append(item)
    return cleanList 

def cleanEscapeCharacters(stringy):
    return stringy.replace('\\', '')

def get_menu_items(eatery):
    r = requests.get(cleanEscapeCharacters(str(get_to_menu(eatery))))
    soup = BeautifulSoup(r.content,"html.parser")

    breakfast = soup.find('div', {'class':'fulldaymenu'})
    lunch = breakfast.find('div', {'class':'fulldaymenu'})
    dinner = lunch.find('div', {'class':'fulldaymenu'})

    dinner_items = dinner.find_all('strong')
    lunch_items = filter(lambda x: x not in dinner_items, lunch.find_all('strong'))
    breakfast_items = filter(lambda x: x not in lunch_items and x not in dinner_items, breakfast.find_all('strong'))

    return map(lambda x: remove_tags_and_encodings(x), [breakfast_items, lunch_items, dinner_items])

print get_menu_items('sharpe-refectory')
print get_menu_items('verney-woolley')



