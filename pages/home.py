import json
from selenium.webdriver.common.by import By

with open('config.json') as config_file:
  config = json.load(config_file)

web = config['web']


class MercadolibreHomePage:

    BUSQUEDA_INPUT = (By.ID,'cb1-edit')
    BUSCAR_BUTTON = (By.CLASS_NAME,'nav-icon-search')

    URL = web 

    def __init__(self,browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)

    def search_input(self,destino):
        self.browser.find_element(*self.BUSQUEDA_INPUT).send_keys(destino)
    
    def buscar(self):
        self.browser.find_element(*self.BUSCAR_BUTTON).click()


