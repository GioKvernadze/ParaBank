from Pages.BasePage import BasePage
from Values.locators import LOGIN_PAGE_LOCATORS

class LoginPage(BasePage):

    def enter_username(self, username):
        self.input_text(LOGIN_PAGE_LOCATORS["USERNAME_FIELD"], username)

    def enter_password(self, password):
        self.input_text(LOGIN_PAGE_LOCATORS["PASSWORD_FIELD"], password)

    def click_login(self):
        self.click(LOGIN_PAGE_LOCATORS["LOGIN_BUTTON"])
