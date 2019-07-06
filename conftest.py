import pytest
import os
from data.testData import URL


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    dic = os.getcwd().replace("conftest.py", "").replace('\\', '/') + "/drivers/chromedriver.exe"
    print(dic)
    driver = webdriver.Chrome(executable_path=dic)
    driver.implicitly_wait(20)
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.quit()
# C:/Users/acer/PycharmProjects/Automation_Framewrok/drivers/chromedriver.exe"