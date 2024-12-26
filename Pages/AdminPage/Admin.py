from Pages.BasePage import BasePage
from Values.locators import ADMIN_LOCATORS
from Helper.DriverSetup import DriverSetup


class AdminPage(BasePage):
    def navigate_to_admin_page(self):
        self.click(ADMIN_LOCATORS["ADMIN_BUTTON"])

    def verify_admin_page_loaded(self):
        return self.wait_for_element(ADMIN_LOCATORS["ADMIN_HEADER"]).is_displayed()

    def initialize_database(self):
        self.click(ADMIN_LOCATORS["INIT_BUTTON"])

    def clean_database(self):
        self.click(ADMIN_LOCATORS["CLEAN_BUTTON"])

    def shutdown_jms_service(self):
        self.click(ADMIN_LOCATORS["SHUTDOWN_JMS_BUTTON"])

    def update_application_settings(self, initial_balance, minimum_balance):
        self.input_text(ADMIN_LOCATORS["INITIAL_BALANCE"], initial_balance, scroll=True)
        self.input_text(ADMIN_LOCATORS["MINIMUM_BALANCE"], minimum_balance, scroll=True)

        self.click(ADMIN_LOCATORS["SUBMIT_BUTTON"], scroll=True)
        print("Submit button clicked successfully after scrolling.")

        success_message_locator = ADMIN_LOCATORS.get("SUCCESS_MESSAGE")
        try:
            success_message = self.wait_for_element(success_message_locator, timeout=15)
            if success_message and success_message.is_displayed():
                print("Settings saved successfully.")
                DriverSetup.take_screenshot(self.driver, "Admin_Settings_Save_Success")
            else:
                raise Exception("Success message is not displayed!")
        except Exception as e:
            DriverSetup.take_screenshot(self.driver, "Admin_Settings_Save_Failure")
            raise Exception(f"Failed to save settings: {e}")
