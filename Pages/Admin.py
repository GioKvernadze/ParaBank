from Pages.BasePage import BasePage
from Values.pathes import ADMIN_LOCATORS

class AdminPage(BasePage):


    def navigate_to_admin_page(self):

        self.wait_for_element_clickable(ADMIN_LOCATORS["ADMIN_BUTTON"]).click()

    def verify_admin_page_loaded(self):

        return self.wait_for_element(ADMIN_LOCATORS["ADMIN_HEADER"]).is_displayed()

    def initialize_database(self):

        self.wait_for_element_clickable(ADMIN_LOCATORS["INIT_BUTTON"]).click()

    def clean_database(self):

        self.wait_for_element_clickable(ADMIN_LOCATORS["CLEAN_BUTTON"]).click()

    def shutdown_jms_service(self):

        self.wait_for_element_clickable(ADMIN_LOCATORS["SHUTDOWN_JMS_BUTTON"]).click()

    def update_application_settings(self, initial_balance, minimum_balance):

        self.scroll_and_input(ADMIN_LOCATORS["INITIAL_BALANCE"], initial_balance)
        self.scroll_and_input(ADMIN_LOCATORS["MINIMUM_BALANCE"], minimum_balance)
        self.wait_for_element_clickable(ADMIN_LOCATORS["SUBMIT_BUTTON"]).click()
