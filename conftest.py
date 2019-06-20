import pytest


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/acer/PycharmProjects/Automation_Framewrok/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("http://localhost/login.do")
    request.cls.driver = driver
    yield
    driver.quit()