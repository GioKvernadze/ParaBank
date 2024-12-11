from Pages.BasePage import BasePage
from Values.pathes import LOGIN_PAGE_LOCATORS

class LoginPage(BasePage):

    def enter_username(self, username):
        self.wait_for_element(LOGIN_PAGE_LOCATORS["USERNAME_FIELD"]).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(LOGIN_PAGE_LOCATORS["PASSWORD_FIELD"]).send_keys(password)

    def click_login(self):
        self.wait_for_element_clickable(LOGIN_PAGE_LOCATORS["LOGIN_BUTTON"]).click()
