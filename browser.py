from selenium import webdriver
import unittest

class Browser(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)

    def close(self):
        self.driver.close()
