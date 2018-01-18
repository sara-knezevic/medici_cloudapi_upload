import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

filename = '26.jpg' # file name
path = os.path.join('/home/saras/coding/medici/receipts/', filename) # file folder
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://cloud.google.com/vision.html")

frame = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/article/section[1]/div[2]/iframe')
driver.switch_to.frame(frame)

upload = driver.find_element_by_xpath("//*[@id='input']").send_keys(path) # upload photo


time.sleep(10) # wait for the image  to process

json_finder = driver.find_element_by_xpath('//*[@id="display"]') 
# get contents of span items in this one ^

html = driver.page_source
soup = BeautifulSoup(html, "lxml")
text = ''
everything_file = open(filename[:-3] + 'txt', 'w')

for a in soup.find('pre', {'id' : 'display'}).findChildren():
	text += '\n'
	text += (a.text)

before, receipt_text = text.split('"textAnnotations":') # splits everything useless before the texts (logos and stuff)
receipt_text, end = receipt_text.split('"safeSearchAnnotation":') # splits everything after (some google things)

receipt = receipt_text.split('"description":')

for t in receipt[2:]: # skips line where the whole text of the receipt is 
					  # and prints to the file the characters
	everything_file.write(t)

everything_file.close()