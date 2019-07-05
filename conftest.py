import pytest
from data.testData import URL


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/acer/PycharmProjects/Automation_Framewrok/drivers/chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.quit()
