from Pages.BasePage import BasePage
from Values.pathes import REGISTER_PAGE_LOCATORS

class RegisterPage(BasePage):
    def enter_name(self, first_name, last_name):
        """
        Enter the first name and last name.
        """
        first_name_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["FIRST_NAME_FIELD"])
        if first_name_field:
            first_name_field.send_keys(first_name)
        else:
            raise Exception("First name field not found!")

        last_name_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["LAST_NAME_FIELD"])
        if last_name_field:
            last_name_field.send_keys(last_name)
        else:
            raise Exception("Last name field not found!")

    def enter_address(self, address, city, state, zip_code):
        """
        Enter the address, city, state, and zip code.
        """
        address_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["ADDRESS_FIELD"])
        if address_field:
            address_field.send_keys(address)
        else:
            raise Exception("Address field not found!")

        city_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["CITY_FIELD"])
        if city_field:
            city_field.send_keys(city)
        else:
            raise Exception("City field not found!")

        state_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["STATE_FIELD"])
        if state_field:
            state_field.send_keys(state)
        else:
            raise Exception("State field not found!")

        zip_code_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["ZIP_CODE_FIELD"])
        if zip_code_field:
            zip_code_field.send_keys(zip_code)
        else:
            raise Exception("Zip code field not found!")

    def enter_contact_info(self, phone_number, ssn):
        """
        Enter the phone number and SSN.
        """
        phone_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["PHONE_FIELD"])
        if phone_field:
            phone_field.send_keys(phone_number)
        else:
            raise Exception("Phone number field not found!")

        ssn_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["SSN_FIELD"])
        if ssn_field:
            ssn_field.send_keys(ssn)
        else:
            raise Exception("SSN field not found!")

    def enter_credentials(self, password, confirm_password):
        """
        Enter the password and confirm it.
        """
        password_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["PASSWORD_FIELD"])
        if password_field:
            password_field.send_keys(password)
        else:
            raise Exception("Password field not found!")

        confirm_password_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["CONFIRM_PASSWORD_FIELD"])
        if confirm_password_field:
            confirm_password_field.send_keys(confirm_password)
        else:
            raise Exception("Confirm password field not found!")

    def enter_username(self, username):
        """
        Enter the username.
        """
        username_field = self.wait_for_element(REGISTER_PAGE_LOCATORS["USERNAME_FIELD"])
        if username_field:
            username_field.send_keys(username)
        else:
            raise Exception("Username field not found!")

    def click_register(self):
        """
        Click the Register button.
        """
        register_button = self.wait_for_element_clickable(REGISTER_PAGE_LOCATORS["REGISTER_BUTTON"])
        if register_button:
            register_button.click()
        else:
            raise Exception("Register button not clickable!")
