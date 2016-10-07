import requests
from bs4 import BeautifulSoup

r = requests.get("http://legacy.cafebonappetit.com/weekly-menu/129506")
soup = BeautifulSoup(r.content,"html.parser")

'''
data = soup.find_all('div', class_ = 'menu-item-description')
item = str(data[0])
splitOne = item.split('<')
meal = (splitOne[10].split('>'))[1]
food = (splitOne[3].split('>'))[1]

#splitTwo = splitOne[3].split('>')
#print(meal)
#print(food)

result = []
for item in data:
	item = str(item)
	splitOne = item.split('<')
	meal = (splitOne[10].split('>'))[1]
	food = (splitOne[3].split('>'))[1]
	result.append(food + ' ' + meal)
#print (result)
'''

newDat = soup.find_all('div', id = 'td-12175-1')
#f = newDat[1]
print(newDat)



#a = soup.find_all(id="td-12305-1")
#print(a)
