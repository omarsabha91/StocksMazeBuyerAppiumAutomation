from appium.webdriver.common.mobileby import MobileBy

class LoginPage:
    """
    LoginPage class represents the login screen and its actions.
    """

    def __init__(self, driver):
        """
        Initializes the login page with the necessary elements.

        :param driver: Appium driver
        """
        self.driver = driver
        self.username_field = (MobileBy.ACCESSIBILITY_ID, "usernameField")
        self.password_field = (MobileBy.ACCESSIBILITY_ID, "passwordField")
        self.login_button = (MobileBy.ACCESSIBILITY_ID, "loginButton")

    def enter_username(self, username):
        """
        Enters the given username into the username field.

        :param username: Username to be entered
        """
        username_element = self.driver.find_element(*self.username_field)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        """
        Enters the given password into the password field.

        :param password: Password to be entered
        """
        password_element = self.driver.find_element(*self.password_field)
        password_element.clear()
        password_element.send_keys(password)

    def press_login_button(self):
        """
        Presses the login button.
        """
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """
        Convenience method to log in using a username and password.

        :param username: Username to be entered
        :param password: Password to be entered
        """
        self.enter_username(username)
        self.enter_password(password)
        self.press_login_button()
