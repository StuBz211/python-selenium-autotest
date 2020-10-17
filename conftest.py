import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = './chromedriver'


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="class")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(executable_path=path, options=options)
    yield browser
    browser.quit()
