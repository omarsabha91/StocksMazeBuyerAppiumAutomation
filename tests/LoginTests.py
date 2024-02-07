from tests.BaseTest import BaseTest
from pages.LoginPage import LoginPage

class LoginTests(BaseTest):
    def test_login_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.login("testuser", "testpassword")

        # Add assertions here to verify login success
