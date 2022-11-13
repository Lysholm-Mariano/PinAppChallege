QA CHALLENGE - PinApp

UI Testing - Selenium and Python

Testing web: Mercadolibre.com

Desing Pattern: Page Object
    objects are created representing components or web pages

What is needed:

- Python 3.8 or higher
- pipenv, "pip install pipenv"
- atomicwrites, "pipenv install atomicwrites"
- Selenium, "pipenv install selenium"
- Correct version of webdrivers for your browsers
    Chromedriver https://chromedriver.chromium.org/downloads
    geckodriver https://github.com/mozilla/geckodriver/releases
- Chromedriver and geckodriver must be on PATH

check everything is set up with
- "Python -V" or "python --version" to show version installed
- "pipenv --version" to show version installed
- "chromedriver --version" "geckodriver --version" or to show version installed



Modify browser in config.json with "Chrome", "Firefox", "headless Chrome"

Install all dependencies for a project:
    $ pipenv install 

run tests:
    $ pipenv run python -m pytest 

run parallel tests:
    $ pipenv run python -m pytest  -n 3
