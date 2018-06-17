from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import requests 
import re
import threading
import queue
import grequests 

chrome = webdriver.Chrome('/Users/armandcroitoru/Downloads/chromedriver')
chrome.get('https://wwww.triburile.ro')

def Logare():

	

	usr = chrome.find_element_by_id('user')
	while usr==[]:
		usr = chrome.find_element_by_id('user')

	# chrome.support.expected_conditions.visibility_of(usr)

	pas = chrome.find_element_by_id('password')
	but = chrome.find_element_by_link_text('Logare')
		
	usr.send_keys('iggprt')
	pas.send_keys('ElilasCC')
	but.click()

	but2 = []
	while but2 == []:
		print (but2)
		try:
			but2 = chrome.find_element_by_link_text('Lumea 64')
		except:
			pass
	but2.click()
	time.slepp(1)
	but.click()
	while():
		but2 = chrome.f

	print ('DONE')

	# chrome.get('https://ro64.triburile.ro/game.php?screen=overview')

Logare()