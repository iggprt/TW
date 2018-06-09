import sqlite3
import requests
import time
from bs4 import BeautifulSoup
import TW_sql



home_link = "http://ro.twstats.com/ro64/index.php?page=village&id="
source = ''
start = time.time()

TW_sql.create_tables()

# for i in range(9163,12000):
# 	source = requests.get(home_link + str(i)).text 
# 	source = source[source.find('Nume:'):source.find('Istoria satului')]

# 	soup = BeautifulSoup (source, 'lxml')
# 	matches = soup.find_all('td')
# 	matches = [match.text for match in matches]
# 	fin = time.time()-start
# 	rate = fin/i

# 	if matches != []:
# 		x = int(matches[1][:3])
# 		y = int(matches[1][4:])

# 		points = int(matches[3].replace(',',''))

# 		TW_sql.append_village(v_id = i, name=matches[0], x=x, y=y, owner=matches[4], tribe=matches[5], continent= matches[2], points=points)
# 	else: 
# 		print (i)

TW_sql.get_villages()



