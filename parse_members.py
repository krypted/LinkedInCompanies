from selenium import webdriver
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
import time
import numpy as np
from selenium.webdriver.common.keys import Keys
import csv
from selenium.common.exceptions import NoSuchElementException

#writer = csv.writer(open('testing.csv', 'w')) # preparing csv file to store parsing result later
#writer.writerow(['name', 'job_title', 'schools', 'location', 'ln_url'])

query_keyword = "companies"
no_of_pages = 1
USERNAME='******@***.com'
PASSWORD='******'

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
urlhome='https://www.linkedin.com/'
driver.get(urlhome)
driver.find_element_by_xpath('//a[text()="Sign in"]').click()
username_input = driver.find_element_by_name('session_key')
username_input.send_keys(USERNAME)
password_input = driver.find_element_by_name('session_password')
password_input.send_keys(PASSWORD)
driver.find_element_by_xpath('//button[text()="Sign in"]').click()


with open("CompaniesNames.txt", "r") as f:
	urls = f.read().splitlines()

with open(query_keyword + ".csv", "a") as file:
	file.write(
		"company name:, #employees: , #companyLink:  ,\n"
	)


for link in (urls):
	driver.get('https://www.linkedin.com/company/'+str(link)+'/')
	Sort = driver.find_element_by_xpath(".//section[@class='org-top-card artdeco-card ember-view']")
	source_code = Sort.get_attribute("outerHTML")
	#print(source_code)
	employees = Sort.find_element_by_xpath(".//div[@class='mt2']")
	members = employees.find_element_by_xpath(".//a[@class='ember-view link-without-visited-state inline-block']")

	print(members.get_attribute('href'))
	print(str(link),":",employees.text[8:])


  #  NumEmplyees1 = section.find_element_by_xpath(".//div[@class='ember-view link-without-visited-state inline-block']")

