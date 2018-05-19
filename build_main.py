from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests 
import re
import threading
import queue
import grequests 
"""
chrome = webdriver.Chrome('/Users/armandcroitoru/Downloads/chromedriver')
chrome.get('https://wwww.triburile.ro')

usr = []
while usr == []:

	usr = chrome.find_element_by_id('user')
	pas = chrome.find_element_by_id('password')
	but = chrome.find_element_by_link_text('Logare')
	
usr.send_keys('iggprt')
pas.send_keys('ElilasCC')
but.click()

time.sleep(1)
but2 = []
while but2 == []:
	but2 = chrome.find_element_by_link_text('Lumea 63')

but2.click()
"""

links = []

index = 0

def get_coord(source):
	global index
	index += 1
	pattern = re.compile(r'[\d]+\|[\d]+')
	results = pattern.findall(source)
	if  results != []:
		return results[0]
	else:
		return str(index)

start = time.time()

for i in range(1,246):
	link = 'http://ro.twstats.com/ro63/index.php?page=village&id=' + str(i)
	links.append(link)

i = 0
for link in links:
	req = requests.get(link)
	print (get_coord(req.text) + " " + str(index))
print (time.time() - start)
index = 0
results = grequests.map((grequests.get(link) for link in links))



results = [result.text for result in results if result != None]

results = [get_coord(result) for result in results]
for r in results:
	print (r)
print (len(results))

print (time.time() - start)