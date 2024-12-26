from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Values.locators import OPEN_NEW_ACCOUNT_LOCATORS

class OpenNewAccountPage(BasePage):

    def navigate_to_open_new_account(self):
        self.click(OPEN_NEW_ACCOUNT_LOCATORS["OPEN_NEW_ACCOUNT"], scroll=True)

    def select_account_type(self, account_type):
        try:
            self.select_option(OPEN_NEW_ACCOUNT_LOCATORS["ACCOUNT_TYPE_DROPDOWN"], value=account_type, scroll=True)
        except Exception as e:
            print(f"Failed to select account type '{account_type}': {e}")
            raise

    def select_from_account(self, account_index):
        try:
            options = self.get_dropdown_options(OPEN_NEW_ACCOUNT_LOCATORS["FROM_ACCOUNT_DROPDOWN"])
            if account_index >= len(options):
                raise Exception(f"Index {account_index} is out of bounds for the dropdown options!")
            self.select_option(OPEN_NEW_ACCOUNT_LOCATORS["FROM_ACCOUNT_DROPDOWN"], index=account_index)
            print(f"Option at index {account_index} selected successfully.")
        except Exception as e:
            raise Exception(f"Failed to select from account with index '{account_index}': {e}")

    def click_open_new_account(self):
        self.click(OPEN_NEW_ACCOUNT_LOCATORS["OPEN_NEW_ACCOUNT_BUTTON"], scroll=True)

    def verify_account_created(self):
        """
        Verifies if the account was created successfully by waiting for the success message header
        and then retrieves the new account number.
        """
        try:
            # Wait for the account opened message header to appear
            header = self.wait_for_element(OPEN_NEW_ACCOUNT_LOCATORS["ACCOUNT_OPENED_MESSAGE"], timeout=10)
            if not header:
                raise Exception("Account opened message header not found!")

            # Retrieve and return the new account number
            account_number_element = self.wait_for_element(OPEN_NEW_ACCOUNT_LOCATORS["NEW_ACCOUNT_NUMBER"], timeout=10)
            if not account_number_element:
                raise Exception("New account number element not found!")

            account_number = account_number_element.text
            print(f"New account created successfully with account number: {account_number}")
            return account_number
        except Exception as e:
            raise Exception(f"Failed to verify account creation: {e}")
