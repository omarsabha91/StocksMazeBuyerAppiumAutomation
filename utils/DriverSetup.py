from appium import webdriver
import os

class DriverSetup:
    @staticmethod
    def get_driver():
        # Define desired capabilities for iOS
        desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '14.4',  # Adjust as needed
            'deviceName': 'iPhone 11',  # Adjust as needed
            'automationName': 'XCUITest',
            'app': os.environ.get('APP_PATH'),  # APP_PATH is an environment variable
            # Additional capabilities as needed
        }

        # Initialize the Appium driver with the desired capabilities
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return driver
