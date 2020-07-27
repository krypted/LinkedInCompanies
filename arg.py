
from selenium import webdriver

#!/usr/bin/python
import argparse
parser = argparse.ArgumentParser(description='This is a demo script by nixCraft.')
parser.add_argument('-username','--input', help='Company Name',required=True)
parser.add_argument('-password','--input1', help='Company Name',required=True)
parser.add_argument('-company','--input2', help='Company Name',required=True)

args = parser.parse_args()  ## show values ##
print (args.input)


#writer = csv.writer(open('testing.csv', 'w')) # preparing csv file to store parsing result later
#writer.writerow(['name', 'job_title', 'schools', 'location', 'ln_url'])

query_keyword = "companies"
no_of_pages = 1


driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
urlhome='https://www.linkedin.com/'
driver.get(urlhome)
driver.find_element_by_xpath('//a[text()="Sign in"]').click()
username_input = driver.find_element_by_name('session_key')
username_input.send_keys(args.input)
password_input = driver.find_element_by_name('session_password')
password_input.send_keys(args.input1)
driver.find_element_by_xpath('//button[text()="Sign in"]').click()


driver.get('https://www.linkedin.com/company/'+str(args.input2)+'/')
Sort = driver.find_element_by_xpath(".//section[@class='org-top-card artdeco-card ember-view']")
source_code = Sort.get_attribute("outerHTML")
#print(source_code)
employees = Sort.find_element_by_xpath(".//div[@class='mt2']")
members = employees.find_element_by_xpath(".//a[@class='ember-view link-without-visited-state inline-block']")

print(str(args.input2),":",employees.text[8:])
print(members.get_attribute('href'))

  #  NumEmplyees1 = section.find_element_by_xpath(".//div[@class='ember-view link-without-visited-state inline-block']")
