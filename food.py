import requests
import re
from bs4 import BeautifulSoup

def removeTags(listy):
    cleanList = []
    for item in listy:
        cleanList.append(re.sub('<\S+>|</\S+>', '', str(item)))
    return cleanList 

r = requests.get("http://legacy.cafebonappetit.com/print-menu/cafe/1531/menu/130593/days/today/pgbrks/0/")
soup = BeautifulSoup(r.content,"html.parser")

breakfast = soup.find('div', {'class':'fulldaymenu'})
lunch = breakfast.find('div', {'class':'fulldaymenu'})
dinner = lunch.find('div', {'class':'fulldaymenu'})
dinner_items = dinner.find_all('strong')
lunch_items = filter(lambda x: x not in dinner_items, lunch.find_all('strong'))
breakfast_items = filter(lambda x: x not in lunch_items and x not in dinner_items, breakfast.find_all('strong'))

print removeTags(dinner_items)
print removeTags(lunch_items)
print removeTags(breakfast_items)

