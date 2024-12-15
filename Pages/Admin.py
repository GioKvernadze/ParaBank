from Pages.BasePage import BasePage
from Values.locators import ADMIN_LOCATORS
from Helper.DriverSetup import DriverSetup  # Import DriverSetup for screenshots


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
        """
        Update application settings and verify submission.
        """
        # Fill in application settings fields
        self.scroll_and_input(ADMIN_LOCATORS["INITIAL_BALANCE"], initial_balance)
        self.scroll_and_input(ADMIN_LOCATORS["MINIMUM_BALANCE"], minimum_balance)

        # Click Submit button
        self.wait_for_element_clickable(ADMIN_LOCATORS["SUBMIT_BUTTON"]).click()
        print("Submit button clicked successfully.")

        # Verify success message
        success_message_locator = ADMIN_LOCATORS.get("SUCCESS_MESSAGE")
        if success_message_locator:
            try:
                success_message = self.wait_for_element(success_message_locator, timeout=5)
                if success_message.is_displayed():
                    print("Settings saved successfully.")
                else:
                    raise Exception("Success message not displayed!")
            except Exception as e:
                # Take a screenshot using DriverSetup
                DriverSetup.take_screenshot(self.driver, "Admin_Settings_Save_Failure")
                raise Exception(f"Failed to save settings: {e}")
        else:
            print("No success message locator defined.")
