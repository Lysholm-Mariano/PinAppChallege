import json
from selenium.webdriver.common.by import By

with open('config.json') as config_file:
  config = json.load(config_file)

web = config['web']

class ResultPage:

    URL = web 

    TITULO_TEXT = (By.XPATH,'/html/body/main/div/div[2]/aside/div[1]/h1')

    def __init__(self,browser):
        self.browser = browser
    
    def get_title(self):
        return self.browser.find_element(*self.TITULO_TEXT).text
    
    def current_url(self):
        return self.browser.current_url


