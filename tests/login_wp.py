import pytest
from pages.HomePageWP import HomePageWP
from pages.LoginPageWP import LoginWP


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = LoginWP(driver)
        lp.wp_login()

    def test_logout(self):
        driver = self.driver
        hp = HomePageWP(driver)
        hp.wp_logout()
