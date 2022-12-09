import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException

class TEST(unittest.TestCase):
    # EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//*[text()='Log in']")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//*[text()='Please enter your password!']")
    BTN_DISABLED = (By.XPATH, "//button[@data-test-id='login-button']")
    SIGN_UP_LINK = (By.LINK_TEXT, "Sign up.")
    LOGIN_LINK = (By.XPATH, "//*[text()='Log In.']")
    PERSONAL_RATIO_SELECT = (By.XPATH, "(//input[@type='radio'])[2]")
    CONTINUE_BTN = (By.XPATH, "//*[text()='CONTINUE']")
    CONTINUE_BTN2 = (By.XPATH, '//button[@data-test-id="first-name-continue-btn"]')
    CONTINUE_BTN3 = (By.XPATH, '//span[contains(.,"CONTINUE")]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    LAST_NAME_INPUT = (By.XPATH, "//input[@type='text']")
    EMAIL_INPUT = (By.XPATH, "//*[@class='MuiInputBase-input MuiFilledInput-input']")
    EMAIL_MESSAGE_ERROR = (By.XPATH, "//p[text()='Please enter a valid email address.']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://jules.app/sign-in")

    def tearDown(self):
        self.driver.quit()

    def test_email(self):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys("ab@gm.ro")
        sleep(1)

    def test_set_password(self):
        self.test_email()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("123")
        sleep(3)

    def test_click_login_button(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
        sleep(3)

    def test_verify_email_error_msg(self):
        self.test_email()
        expected_msg = "Please enter your password!"
        try:
            actual_msg = self.driver.find_element(*self.PASSWORD_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_msg = "None"                 # nu s-a gasit elementul
        assert actual_msg != expected_msg, f"Error! The message is not displayed{actual_msg}, and expected{expected_msg}"
        sleep(3)

    def test_verify_login_button_disabled(self):
        self.test_email()
        elem_login_btn = self.driver.find_element(*self.BTN_DISABLED)
        self.assertFalse(elem_login_btn.is_enabled(), "Button LOGIN it is not disabled")
        sleep(3)

    def test_click_sign_up_link(self):
        self.driver.find_element(*self.SIGN_UP_LINK).click()
        sleep(2)

    def test_test3(self):
        self.driver.find_element(*self.SIGN_UP_LINK).click()
        sleep(1)
        self.driver.find_element(*self.PERSONAL_RATIO_SELECT).click()
        sleep(1)
        self.driver.find_element(*self.CONTINUE_BTN).click()
        sleep(1)
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys("firstname")
        self.driver.find_element(*self.CONTINUE_BTN).click()
        sleep(1)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys("lastname")
        self.driver.find_element(*self.CONTINUE_BTN).click()
        sleep(1)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys("email@gmail.com")
        sleep(2)
        expected_message = "None"
        try:
            actual_message = self.driver.find_element(*self.EMAIL_MESSAGE_ERROR).text
        except NoSuchElementException:
            actual_message = "None"  # nu s-a gasit elementul
        assert actual_message == expected_message, f'Error! The message is incorrect, expected {expected_message}, actual {actual_message}'

        # self.driver.find_element(*self.EMAIL_INPUT).click()
        # sleep(3)
        # self.driver.find_element(*self.EMAIL_INPUT).click()
        # sleep(3)
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(Keys.CONTROL + "A" + Keys.DELETE)
        # sleep(3)
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys("email@gmail.com")
        # sleep(3)
