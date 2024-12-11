import pytest
import allure
from Values.urls import BASE_URL
from Pages.Login import LoginPage
from Values.REGISTER_DATA import register_data
from Helper.DriverSetup import DriverSetup
from Helper.logger import setup_logger

# Initialize logger
logger = setup_logger()

@allure.feature("User Login")
@allure.story("Login with existing user credentials")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_existing_user(driver):

    with allure.step("Retrieve user credentials from saved data"):
        try:
            logger.info("Retrieving user credentials from saved data.")
            data = register_data()
            username = data["Username"]
            password = data["Password"]
            logger.info(f"Using username: {username}")
            allure.attach(f"Username: {username}\nPassword: {password}", name="Login Credentials", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error(f"Failed to retrieve credentials: {e}")
            pytest.fail("Failed to retrieve login credentials.")

    with allure.step("Navigate to the login page"):
        try:
            logger.info("Navigating to the login page.")
            driver.get(BASE_URL)
            DriverSetup.take_screenshot(driver, name="Login Page")
            allure.attach(driver.current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error(f"Failed to navigate to the login page: {e}")
            DriverSetup.take_screenshot(driver, name="Navigation Error")
            pytest.fail("Navigation to login page failed.")

    with allure.step("Enter login credentials"):
        try:
            logger.info("Entering login credentials.")
            login_page = LoginPage(driver)
            login_page.enter_username(username)
            login_page.enter_password(password)
            DriverSetup.take_screenshot(driver, name="Credentials Entered")
        except Exception as e:
            logger.error(f"Failed to enter login credentials: {e}")
            DriverSetup.take_screenshot(driver, name="Credentials Error")
            pytest.fail("Failed to enter login credentials.")

    with allure.step("Submit login form"):
        try:
            logger.info("Submitting login form.")
            login_page.click_login()
            DriverSetup.take_screenshot(driver, name="After Submit")
        except Exception as e:
            logger.error(f"Failed to submit login form: {e}")
            DriverSetup.take_screenshot(driver, name="Submit Error")
            pytest.fail("Failed to submit login form.")

    with allure.step("Verify successful login"):
        try:
            success_message = "Accounts Overview"
            assert success_message in driver.page_source, "Login failed!"
            logger.info("Login successful. Accounts Overview found.")
            DriverSetup.take_screenshot(driver, name="Login Success")
            allure.attach(driver.page_source, name="Page Source", attachment_type=allure.attachment_type.TEXT)
        except AssertionError as e:
            logger.error("Login verification failed. 'Accounts Overview' not found.")
            DriverSetup.take_screenshot(driver, name="Login Failed")
            pytest.fail("Login failed! Verification unsuccessful.")
        except Exception as e:
            logger.error(f"Unexpected error during login verification: {e}")
            DriverSetup.take_screenshot(driver, name="Login Verification Error")
            pytest.fail("Unexpected error during login verification.")

    logger.info("Test for user login completed successfully.")
