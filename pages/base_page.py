from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(Browser):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver,25).until(EC.presence_of_element_located((by,selector)))

    def wait_and_click_elem(self, by, selector):
        WebDriverWait(self.driver,25).until(EC.presence_of_element_located((by,selector)))
        self.driver.find_element(by, selector).click()

    def url_check(self, expected_url):
        actual_url = self.driver.current_url
        self.assertEqual(actual_url,expected_url,"The url is incorrect")