from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests 
import re
import threading
import queue
import grequests 

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

time.sleep(2)
but2 = chrome.find_element_by_link_text('Lumea 64')
but2 = chrome.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[10]/div[3]/div[2]/div[1]/a[2]/span')
but2.click()
time.sleep(2)

but = chrome.find_element_by_link_text('Piaţa centrală')
but.click()
time.sleep(1)

lanc = chrome.find_element_by_id('unit_input_spear')
lanc.send_keys(4)
coord = chrome.find_element_by_xpath('//*[@id="place_target"]/input')
coord.send_keys('585|517')

but = chrome.find_element_by_xpath('//*[@id="target_attack"]')
but.click()

time.sleep(2)
but = chrome.find_element_by_xpath('//*[@id="command-data-form"]')
but.click()



