class StorePage:
    def __init__(self, driver):
        self.driver = driver
        self.unique_element_locator = ("id", "unique_element_id_for_store_page")

    def has_unique_element(self):
        """Check if the unique element for the Store page is present."""
        try:
            self.driver.find_element(*self.unique_element_locator)
            return True
        except:
            return False
