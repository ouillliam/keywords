from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys

class ChromeBrowser:

    def __init__(self, query, headless = True):
        self.query = query
        self.options = Options()

        if headless:
            self.options.add_argument("headless")

        self.driver = webdriver.Chrome(options=self.options)

    def search(self):
        base_url = "https://www.google.fr/search?q="
        self.browse(base_url + self.query)

    def browse(self, url):
        try:
            self.driver.get(url)
        except:
            print("Error browsing")


    def get_links(self):
        link_class_name = "yuRUbf"
        search_results = self.driver.find_elements_by_class_name(link_class_name)
        link_elements = [result.find_element_by_tag_name('a') for result in search_results]
        links_href = [link.get_attribute('href') for link in link_elements] 
        return links_href
        
        
    def get_current_page_text(self):
        body = self.driver.find_element_by_tag_name('body')
        return body.text