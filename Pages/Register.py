from Pages.BasePage import BasePage
from Values.locators import REGISTER_PAGE_LOCATORS

class RegisterPage(BasePage):

    def enter_name(self, first_name, last_name):
        self.wait_for_element(REGISTER_PAGE_LOCATORS["FIRST_NAME_FIELD"]).send_keys(first_name)
        self.wait_for_element(REGISTER_PAGE_LOCATORS["LAST_NAME_FIELD"]).send_keys(last_name)

    def enter_address(self, address, city, state, zip_code):
        self.wait_for_element(REGISTER_PAGE_LOCATORS["ADDRESS_FIELD"]).send_keys(address)
        self.wait_for_element(REGISTER_PAGE_LOCATORS["CITY_FIELD"]).send_keys(city)
        self.wait_for_element(REGISTER_PAGE_LOCATORS["STATE_FIELD"]).send_keys(state)
        self.wait_for_element(REGISTER_PAGE_LOCATORS["ZIP_CODE_FIELD"]).send_keys(zip_code)

    def enter_contact_info(self, phone_number, ssn):
        self.wait_for_element(REGISTER_PAGE_LOCATORS["PHONE_FIELD"]).send_keys(phone_number)
        self.wait_for_element(REGISTER_PAGE_LOCATORS["SSN_FIELD"]).send_keys(ssn)

    def enter_username(self, username):
        self.wait_for_element(REGISTER_PAGE_LOCATORS["USERNAME_FIELD"]).send_keys(username)

    def enter_credentials(self, password, confirm_password):

        self.wait_for_element(REGISTER_PAGE_LOCATORS["PASSWORD_FIELD"]).send_keys(password)
        self.scroll_and_input(REGISTER_PAGE_LOCATORS["CONFIRM_PASSWORD_FIELD"], confirm_password)

    def click_register(self):
        self.wait_for_element_clickable(REGISTER_PAGE_LOCATORS["REGISTER_BUTTON"]).click()
