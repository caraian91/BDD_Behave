from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class SignUpPage(BasePage):
    # Atributs
    SIGN_UP_LINK = (By.LINK_TEXT, "Sign up.")
    LOGIN_LINK = (By.XPATH, "//*[text()='Log In.']")
    PERSONAL_RATIO_SELECT = (By.XPATH, "(//input[@type='radio'])[2]")
    CONTINUE_BTN = (By.XPATH, "//span[contains(.,'CONTINUE')]")
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    LAST_NAME_INPUT = (By.XPATH, "//input[@type='text']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    EMAIL_MESSAGE_ERROR = (By.XPATH, "//p[text()='Please enter a valid email address.']")

    # Methods
    # metoda creata in BasePage
    def click_sign_up_link(self):
        self.wait_and_click_elem(*self.SIGN_UP_LINK)

    # metoda creata in BasePage
    def verify_url_signup(self):
        self.url_check("https://jules.app/sign-up")

    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def verify_url_sign_in(self):
        self.url_check("https://jules.app/sign-in")

    def select_ratio_personal(self):
        self.driver.find_element(*self.PERSONAL_RATIO_SELECT).click()

    # metoda creata in BasePage
    def click_continue_button(self):
        self.wait_and_click_elem(*self.CONTINUE_BTN)

    def set_first_name(self, firstname):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(lastname)

    def set_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def verify_email_error_msg(self, expected_msg):
        try:
            actual_msg = self.driver.find_element(*self.EMAIL_MESSAGE_ERROR).text
        except NoSuchElementException:
            actual_msg = "None"  # nu s-a gasit eroarea
        assert actual_msg == expected_msg, f'Error! The message is not diplayed or incorrect, expected {expected_msg}, actual {actual_msg}'


    def clear_email_input(self):
        self.driver.find_element(*self.EMAIL_INPUT).click()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(Keys.CONTROL + "A" + Keys.DELETE)
