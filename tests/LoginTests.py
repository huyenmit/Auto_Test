import csv
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.Page_login import txt_username, txt_password, bt_login
from utils.CustomChromeDriver import customChrome
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import VerifyLogin


class MyTestCase(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_argument('--disable-notifications')
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_argument("start-maximized")
        self.drivers = webdriver.Chrome(chrome_options=option, executable_path="../drivers/chromedriver.exe")
        self.drivers.implicitly_wait(3)


        links = readDatatest.getLink('../linkFile.csv')
        for item in links:
            if item[0] == 'Login':
                self._dataTestAll = readDatatest.dataTestLogin(item[1])
                self._dataTest = self._dataTestAll[0]

    def tearDown(self):
        self.drivers.quit()

    def test_login(self):
        self.drivers.get(self._dataTest[2])
        stepLogin(self.drivers).login(self._dataTest[0], self._dataTest[1])
        time.sleep(5)
        self.expect = VerifyLogin(self.drivers).login()
        self.assertIn(self._dataTest[3], self.expect, "Login fail")

    if __name__ == "__main__":
        unittest.main(testRunner=HTMLTestRunner(output="reports"))

