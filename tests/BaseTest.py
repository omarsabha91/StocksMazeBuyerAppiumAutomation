import unittest
from utils.DriverSetup import DriverSetup

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverSetup.get_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
