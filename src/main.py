from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
import browser

browser = browser.ChromeBrowser("vélo annecy")
# browser.search()
# links = browser.get_links()
# print(links)

browser.browse("https://annecy.yoga/")
text = browser.get_current_page_text()
print(text)
browser.driver.close()