import unittest
from BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.StorePage import StorePage
from pages.SettingsPage import SettingsPage
from pages.ProfilePage import ProfilePage  # Import the ProfilePage


class NavigationTest(BaseTest):
    def test_navigation_through_pages(self):
        """Test sequential navigation from Home to Store to Settings to Profile."""
        # Navigate from Home to Store
        home_page = HomePage(self.driver)
        home_page.bottom_nav_bar.navigate_to_store()

        # Verify navigation to Store
        store_page = StorePage(self.driver)
        self.assertTrue(store_page.has_unique_element(), "Failed to navigate to Store page")

        # Navigate from Store to Settings
        store_page.bottom_nav_bar.navigate_to_settings()

        # Verify navigation to Settings
        settings_page = SettingsPage(self.driver)
        self.assertTrue(settings_page.has_unique_element(), "Failed to navigate to Settings page")

        # Navigate from Settings to Profile
        settings_page.bottom_nav_bar.navigate_to_profile()  # This assumes you have a navigate_to_profile method

        # Verify navigation to Profile
        profile_page = ProfilePage(self.driver)
        self.assertTrue(profile_page.has_unique_element(), "Failed to navigate to Profile page")


if __name__ == "__main__":
    unittest.main()
