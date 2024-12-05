import pytest
from Values.urls import BASE_URL
from Helper.DriverSetup import driver
from Helper.logger import setup_logger
from Pages.Login import LoginPage
from Values.REGISTER_DATA import register_data

# Initialize the logger
logger = setup_logger()

def test_login_existing_user(driver):
    """
    Test logging in with existing user credentials.
    """
    logger.info("Starting the test for logging in with existing user credentials.")

    # Navigate to the login page
    try:
        logger.info("Navigating to the login page.")
        driver.get(BASE_URL)
        logger.info("Successfully navigated to the login page.")
    except Exception as e:
        logger.error(f"Error while navigating to the login page: {e}")
        raise

    # Initialize the LoginPage and use data from the registration
    try:
        login_page = LoginPage(driver)
        data = register_data()  # Use the same function to retrieve credentials

        logger.info(f"Logging in with username: {data['Username']} and password: {data['Password']}")
        login_page.enter_username(data["Username"])
        login_page.enter_password(data["Password"])
        login_page.click_login()
        logger.info("Login submitted successfully.")
    except Exception as e:
        logger.error(f"Error during login process: {e}")
        raise

    # Verify successful login
    try:
        # Replace this with an actual condition to verify successful login
        if "Accounts Overview" in driver.page_source:
            logger.info("Login completed successfully!")
        else:
            logger.error("Login failed. Expected 'Account Overview' text not found.")
            raise AssertionError("Login failed.")
    except Exception as e:
        logger.error(f"Error while verifying login: {e}")
        raise

    logger.info("Login test completed successfully.")
