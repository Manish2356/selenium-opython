import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait




@pytest.fixture(scope="class")
def setup(request):
    serv_obj = Service("C:\\browser drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()