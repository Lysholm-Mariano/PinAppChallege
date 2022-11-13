#shared fixtures
import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'): #read it once

    with open('config.json') as config_file: #reading json File
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome'] #validate values from config file
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()  #Initialize Firefox Instance
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()  #Initialize Chrome Instance
    elif config['browser'] == 'Headless Chrome':
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('headless')
        b = selenium.webdriver.Chrome(options=options)  #Initialize Chrome Instance with no visualization
    else:
        raise Exception("Browser is not supported")


    yield b                          #Return to webDriver

    b.quit()                         #Quit Instance