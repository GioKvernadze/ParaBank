class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        """
        Click the login button on the Home Page.
        """
        login_button = self.driver.find_element_by_id("loginBtn")
        login_button.click()

    def get_page_title(self):
        """
        Return the page title.
        """
        return self.driver.title
