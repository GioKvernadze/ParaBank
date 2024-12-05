import pytest
from Values.urls import REGISTER_URL
from Helper.DriverSetup import driver
from Helper.logger import setup_logger
from Pages.Register import RegisterPage
from Values.REGISTER_DATA import register_data
import os

# Print the current working directory for debugging
print(f"Current working directory: {os.getcwd()}")

# Initialize the logger
logger = setup_logger()
print("Logger initialized successfully in Register_test.py")

def test_register_new_user(driver):
    """
    Test registration with dynamically generated data.
    """
    logger.info("Starting the test for new user registration.")
    # Generate new data for registration
    logger.info("Generating new user data for registration.")
    data = register_data(generate_new=True)  # Force new user creation
    # Navigate to the registration page
    try:
        logger.info("Navigating to the registration page.")
        driver.get(REGISTER_URL)
        logger.info("Successfully navigated to the registration page.")
    except Exception as e:
        logger.error(f"Error while navigating to the registration page: {e}")
        raise

    # Initialize the RegisterPage and generate data
    try:
        register_page = RegisterPage(driver)
        data = register_data()
        logger.info("Generated random registration data:")
        for key, value in data.items():
            logger.info(f"  {key}: {value}")
    except Exception as e:
        logger.error(f"Error while generating test data or initializing the page: {e}")
        raise

    # Fill in the registration form
    try:
        logger.info("Filling in user details.")
        register_page.enter_name(data["FirstName"], data["LastName"])
        register_page.enter_address(data["Address"], data["City"], data["State"], data["ZipCode"])
        register_page.enter_contact_info(data["Phone"], data["SSN"])
        register_page.enter_username(data["Username"])
        register_page.enter_credentials(data["Password"], data["Confirm"])
        logger.info("User details filled successfully.")
    except Exception as e:
        logger.error(f"Error while filling the form: {e}")
        raise

    # Submit the form
    try:
        logger.info("Submitting the registration form.")
        register_page.click_register()
        logger.info("Form submitted successfully.")
    except Exception as e:
        logger.error(f"Error while submitting the form: {e}")
        raise

    # Final logging to mark test completion
    logger.info("Registration test completed successfully.")
