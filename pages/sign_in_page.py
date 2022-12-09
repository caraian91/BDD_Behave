from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class SignInPage(BasePage):
    # Atributs
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//*[text()='Log in']")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//*[@class='MuiFormHelperText-root MuiFormHelperText-contained']")
    BTN_DISABLED = (By.XPATH, "//button[@data-test-id='login-button']")


    # Methods
    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')
        sleep(3)

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def verify_password_error_message(self):
        expected_msg = "Please enter your password!"
        try:
            actual_msg = self.driver.find_element(*self.PASSWORD_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_msg = "None"  # nu s-a gasit elementul
        assert actual_msg != expected_msg, f"Error! The message is not displayed {actual_msg}, and expected {expected_msg}"

    def verify_login_button_disabled(self):
        elem_login_btn = self.driver.find_element(*self.BTN_DISABLED)
        self.assertFalse(elem_login_btn.is_enabled(), "Button LOGIN it is not disabled")

