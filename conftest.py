import pytest
import os
@pytest.fixture(scope='class')
def pre_and_post_action(request):
    from selenium import webdriver
    dir = os.getcwd() + "\\Drivers"
    driver = webdriver.Chrome(dir+"\\chromedriver")
    driver.get('https://google.com')
    driver.get('https://demo.actitime.com')
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver