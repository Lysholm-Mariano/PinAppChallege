import pytest
from common_functions import csv_to_list
from pages.home import MercadolibreHomePage
from pages.result import ResultPage

search_options = csv_to_list(r'.\data\search_options.csv') #Makes a List from a csv with search options

@pytest.mark.parametrize('description',search_options)
def test_search_products(browser,description):
    home_page = MercadolibreHomePage(browser)
    result_page = ResultPage(browser)

    home_page.load()                        #Loads MercadoLibre's Homepage
    home_page.search_input(description)     #types text in input box
    home_page.buscar()                      #Presses search Button

    result_title = result_page.get_title()  #Gets title
    current_url = result_page.current_url() #gets url

    assert description in result_title      #Verifies if the description is included in the title of the search
    assert description in current_url       #Verifies if the description is included in the url of the website

    