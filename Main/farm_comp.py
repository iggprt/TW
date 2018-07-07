import tkinter as tk
import threading
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

class farming():
	def __init__(self):
		# self.chrome = webdriver.Chrome('/Users/armandcroitoru/Downloads/chromedriver')
		self.chrome = webdriver.Chrome('/home/elilas/Downloads/chromedriver')
		self.chrome.get('https://wwww.triburile.ro')
		usr = self.chrome.find_element_by_id('user')
		pas = self.chrome.find_element_by_id('password')
		but = self.chrome.find_element_by_link_text('Logare')
		usr.send_keys('iggprt')
		pas.send_keys('ElilasCC')
		but.click()

		# from selenium.webdriver.support import expected_conditions as EC

		# wait = WebDriverWait(self.chrome, 10)
		# element = wait.until(EC.element_to_be_clickable((By.Id, '//*[@id="home"]/div[3]/div[3]/div[10]/div[3]/div[2]/div[1]/a[2]/span')))

		time.sleep(0.5)
		self.chrome.get('https://wwww.triburile.ro/page/play/ro64')
		self.chrome.get('https://ro64.triburile.ro/game.php?village=8947&screen=place')

	def attack(self,vill):
		x = vill[:vill.find('|')]
		y = vill[vill.find('|') + 1 : ]

		lanc = self.chrome.find_element_by_id('unit_input_light')
		lanc.send_keys(3)
		v = self.chrome.find_element_by_xpath('//*[@id="place_target"]/input')
		v.send_keys(str(x) + str(y))
		but = self.chrome.find_element_by_xpath('//*[@id="target_attack"]')
		but.click()

		# from selenium.webdriver.support import expected_conditions as EC

		wait = WebDriverWait(self.chrome, 10)
		element = wait.until(EC.element_to_be_clickable((By.ID, 'troop_confirm_go')))

		but2 = self.chrome.find_element_by_xpath('//*[@id="troop_confirm_go"]')
		but2.click()

	def rec_attack(self):
		f = open('villages.txt', 'r')
		for v in f:
			try:
				frame = self.chrome.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
				self.chrome.switch_to.frame(frame)
				x = self.chrome.find_element_by_xpath("//*[@id='recaptcha-anchor']")
				self.chrome.switch_to.default_content()
			except selenium.common.exceptions.NoSuchElementException:
				x = None

			print (x)
			self.attack(v)

		#self.attack('588|512')


		#threading.Timer(10, self.rec_attack).start()


f = farming()
f.rec_attack()
