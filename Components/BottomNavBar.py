class BottomNavBar:
    def __init__(self, driver):
        self.driver = driver
        self.home_button_locator = ("id", "com.stocksmaze.buyer:id/iv_dashboard")
        self.stores_button_locator = ("id", "com.stocksmaze.buyer:id/iv_store")
        self.profile_button_locator = ("id", "com.stocksmaze.buyer:id/iv_settings")

    def navigate_to_home(self):
        self.driver.find_element_by_locator(self.home_button_locator).click()

    def navigate_to_stores(self):
        self.driver.find_element_by_locator(self.stores_button_locator).click()

    def navigate_to_profile(self):
        self.driver.find_element_by_locator(self.profile_button_locator).click()
