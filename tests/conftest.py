import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base


@pytest.fixture()
def set_up():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    return driver
