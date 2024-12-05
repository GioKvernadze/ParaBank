from Pages.BasePage import BasePage
from Values.pathes import LOGIN_PAGE_LOCATORS

class LoginPage(BasePage):
    def enter_username(self, username):
        """
        Enter the username in the login form.
        """
        username_field = self.wait_for_element(LOGIN_PAGE_LOCATORS["USERNAME_FIELD"])
        if username_field:
            username_field.send_keys(username)
        else:
            raise Exception("Username field not found!")

    def enter_password(self, password):
        """
        Enter the password in the login form.
        """
        password_field = self.wait_for_element(LOGIN_PAGE_LOCATORS["PASSWORD_FIELD"])
        if password_field:
            password_field.send_keys(password)
        else:
            raise Exception("Password field not found!")

    def click_login(self):
        """
        Click the login button.
        """
        login_button = self.wait_for_element_clickable(LOGIN_PAGE_LOCATORS["LOGIN_BUTTON"])
        if login_button:
            login_button.click()
        else:
            raise Exception("Login button not found!")
