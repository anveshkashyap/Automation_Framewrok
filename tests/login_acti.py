import pytest
from pages.HomePage import HomePage
from pages.LoginPage import Login


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = Login(driver)
        lp.acti_login()

    def test_logout(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.acti_logout()
