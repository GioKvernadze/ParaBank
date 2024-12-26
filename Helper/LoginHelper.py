from Pages.LoginPage.Login import LoginPage
from Pages.RegisterPage.Register import RegisterPage
from Values.urls import BASE_URL, REGISTER_URL
from Values.register_data import register_data
from Helper.DriverSetup import DriverSetup
from selenium.common.exceptions import NoSuchElementException


class LoginHelper:
    def __init__(self, driver):
        self.driver = driver

    def perform_login(self):
        """
        Attempt to perform login with existing credentials.
        """
        try:
            data = register_data()  # Retrieve saved credentials
            username = data["Username"]
            password = data["Password"]

            # Navigate to login page and attempt login
            self.driver.get(BASE_URL)
            login_page = LoginPage(self.driver)

            login_page.enter_username(username)
            DriverSetup.take_screenshot(self.driver, name="After_Username_Entered")

            login_page.enter_password(password)
            DriverSetup.take_screenshot(self.driver, name="After_Password_Entered")

            login_page.click_login()
            DriverSetup.take_screenshot(self.driver, name="After_Login_Clicked")

            # Verify login success
            if "Accounts Overview" in self.driver.page_source:
                print("[INFO] User successfully logged in.")
                return True
            elif "Error!" in self.driver.page_source:  # Check for error message
                print("[ERROR] Login failed due to server error.")
                return False
            else:
                print("[ERROR] Login failed for an unknown reason.")
                return False
        except NoSuchElementException as e:
            print(f"[ERROR] Login failed due to exception: {e}")
            return False

    def perform_registration(self):
        """
        Perform user registration and return the new credentials.
        """
        self.driver.get(REGISTER_URL)
        register_page = RegisterPage(self.driver)
        data = register_data(generate_new=True)

        register_page.enter_name(data["FirstName"], data["LastName"])
        register_page.enter_address(data["Address"], data["City"], data["State"], data["ZipCode"])
        register_page.enter_contact_info(data["Phone"], data["SSN"])
        register_page.enter_username(data["Username"])
        register_page.enter_credentials(data["Password"], data["Confirm"])
        register_page.click_register()

        print("[INFO] Registration completed successfully.")
        DriverSetup.take_screenshot(self.driver, "registration_completed")
        return data

    def login_with_fallback(self):
        """
        Attempt login and perform registration if necessary.
        """
        if not self.perform_login():
            print("[WARNING] Retrying login after registration...")
            self.perform_registration()
            print("[INFO] Skipping login attempt after successful registration.")
