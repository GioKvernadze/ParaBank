from Pages.BasePage import BasePage
from Values.locators import OPEN_NEW_ACCOUNT_LOCATORS

class OpenNewAccountPage(BasePage):

    def navigate_to_open_new_account(self):
        """
        Navigate to the 'Open New Account' page by clicking the link.
        """
        self.wait_for_element_clickable(OPEN_NEW_ACCOUNT_LOCATORS["OPEN_NEW_ACCOUNT"]).click()

    def select_account_type(self, account_type):
        """
        Select the account type (e.g., CHECKING or SAVINGS) by visible text.
        """
        self.select(OPEN_NEW_ACCOUNT_LOCATORS["ACCOUNT_TYPE_DROPDOWN"], value=account_type)

    def select_from_account(self, account_index):
        """
        Select the 'From Account' option by index.
        """
        self.select(OPEN_NEW_ACCOUNT_LOCATORS["FROM_ACCOUNT_DROPDOWN"], index=account_index)

    def click_open_new_account(self):
        """
        Click the 'Open New Account' button.
        """
        self.wait_for_element_clickable(OPEN_NEW_ACCOUNT_LOCATORS["OPEN_NEW_ACCOUNT_BUTTON"]).click()

    def verify_account_created(self):
        """
        Verify that the account was created successfully.
        Returns the account number if created, otherwise returns None.
        """
        success_message = self.wait_for_element(OPEN_NEW_ACCOUNT_LOCATORS["ACCOUNT_OPENED_MESSAGE"])
        if success_message.is_displayed():
            account_number = self.wait_for_element(OPEN_NEW_ACCOUNT_LOCATORS["NEW_ACCOUNT_NUMBER"]).text
            return account_number
        return None
