from appium import webdriver
import os

class DriverSetup:
    @staticmethod
    def get_driver():
        # Define desired capabilities for Android
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': 'Pixel 6 Pro',  # Adjust as needed
            'automationName': 'uiautomator2',
            'app': os.environ.get('APP_PATH'),  # Ensure APP_PATH points to your .apk file
            'avd': 'Pixel_6_Pro'  # Only needed if using an emulator
            # Additional capabilities as needed
        }

        # Initialize the Appium driver with the desired capabilities
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        return driver
