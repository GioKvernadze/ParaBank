import pytest
import allure
from Pages.Login import LoginPage
from Values.urls import BASE_URL
from Values.REGISTER_DATA import register_data
from Helper.DriverSetup import DriverSetup
from Helper.logger import setup_logger

logger = setup_logger()

@allure.feature("User Login")
@allure.story("Verify Login Functionality")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_functionality(driver):
    """
    Explicitly test login functionality using credentials from REGISTER_DATA.
    """
    with allure.step("Retrieve saved user credentials"):
        try:
            data = register_data()
            username = data["Username"]
            password = data["Password"]
            allure.attach(f"Username: {username}\nPassword: {password}", name="Login Credentials")
            logger.info(f"Using Username: {username}")
        except Exception as e:
            logger.error(f"Failed to retrieve login data: {e}")
            pytest.fail("Unable to retrieve user credentials!")

    with allure.step("Navigate to Login Page"):
        try:
            driver.get(BASE_URL)
            DriverSetup.take_screenshot(driver, "Login_Page")
            logger.info("Navigated to Login Page.")
        except Exception as e:
            logger.error(f"Failed to load login page: {e}")
            pytest.fail("Failed to load login page!")

    with allure.step("Enter login credentials and submit"):
        try:
            login_page = LoginPage(driver)
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()
            DriverSetup.take_screenshot(driver, "After_Submit")
            logger.info("Submitted login form.")
        except Exception as e:
            logger.error(f"Failed during login submission: {e}")
            pytest.fail("Failed during login submission.")

    with allure.step("Verify successful login"):
        try:
            assert "Accounts Overview" in driver.page_source, "Login verification failed!"
            DriverSetup.take_screenshot(driver, "Login_Success")
            logger.info("Login successful!")
        except AssertionError:
            logger.error("Login failed: 'Accounts Overview' not found!")
            DriverSetup.take_screenshot(driver, "Login_Failed")
            pytest.fail("Login failed! Could not verify Accounts Overview.")
