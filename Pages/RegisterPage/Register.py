from Pages.BasePage import BasePage
from Values.locators import REGISTER_PAGE_LOCATORS

class RegisterPage(BasePage):

    def enter_name(self, first_name, last_name):
        self.input_text(REGISTER_PAGE_LOCATORS["FIRST_NAME_FIELD"], first_name)
        self.input_text(REGISTER_PAGE_LOCATORS["LAST_NAME_FIELD"], last_name)

    def enter_address(self, address, city, state, zip_code):
        self.input_text(REGISTER_PAGE_LOCATORS["ADDRESS_FIELD"], address)
        self.input_text(REGISTER_PAGE_LOCATORS["CITY_FIELD"], city)
        self.input_text(REGISTER_PAGE_LOCATORS["STATE_FIELD"], state)
        self.input_text(REGISTER_PAGE_LOCATORS["ZIP_CODE_FIELD"], zip_code)

    def enter_contact_info(self, phone_number, ssn):
        self.input_text(REGISTER_PAGE_LOCATORS["PHONE_FIELD"], phone_number)
        self.input_text(REGISTER_PAGE_LOCATORS["SSN_FIELD"], ssn)

    def enter_username(self, username):
        self.input_text(REGISTER_PAGE_LOCATORS["USERNAME_FIELD"], username)

    def enter_credentials(self, password, confirm_password):
        self.input_text(REGISTER_PAGE_LOCATORS["PASSWORD_FIELD"], password)
        self.input_text(REGISTER_PAGE_LOCATORS["CONFIRM_PASSWORD_FIELD"], confirm_password, scroll=True)

    def click_register(self):
        self.click(REGISTER_PAGE_LOCATORS["REGISTER_BUTTON"], scroll=True)
