from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage

# se ruleaza inainte de fiecare test
def before_all(context):
    context.base_page = BasePage()
    context.sign_in_page = SignInPage()
    context.sign_up_page = SignUpPage()

# se ruleaza dupa test
def after_all(context):
    context.browser.close()