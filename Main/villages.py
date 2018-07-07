import sqlite3
import requests
import time
from bs4 import BeautifulSoup
import map_sql
import math



home_link = "http://ro.twstats.com/ro64/index.php?page=village&id="
source = ''
start = time.time()

map_sql.create_tables()
for i in range(1012, 200000):
	source = requests.get(home_link + str(i)).text 
	source = source[source.find('Nume:'):source.find('Istoria satului')]

	soup = BeautifulSoup (source, 'lxml')
	matches = soup.find_all('td')
	matches = [match.text for match in matches]
	fin = time.time()-start
	if i > 0:
		rate = fin/i
	else: 
		rate = 0
	if i%100 == 0:
		print (rate)

	if matches != []:
		x = int(matches[1][:3])
		y = int(matches[1][4:])

		points = int(matches[3].replace(',',''))

		distance = ((x-588)**2 + (y-513)**2)**(1./2)
		distance = float('%.2f' % distance)

		map_sql.append_village(v_id = i, name=matches[0], x=x, y=y, owner=matches[4], tribe=matches[5], continent= matches[2], points=points, distance = distance)
	else: 
		if i%30 == 0:
			print (i)

# map_sql.get_villages()



