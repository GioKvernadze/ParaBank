import pytest
import allure
from Pages.Register import RegisterPage
from Helper.DriverSetup import DriverSetup
from Helper.logger import setup_logger
from Values.urls import REGISTER_URL
from Values.REGISTER_DATA import register_data

# Initialize logger
logger = setup_logger()

@allure.feature("User Registration")
@allure.story("Register a new user with dynamically generated data")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_new_user(driver):

    with allure.step("Generate user data"):
        logger.info("Generating new user data.")
        data = register_data(generate_new=True)
        logger.info(f"Generated user data: {data}")
        allure.attach(str(data), name="Generated User Data", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Navigate to the registration page"):
        try:
            logger.info("Navigating to the registration page.")
            driver.get(REGISTER_URL)
            logger.info(f"Current URL: {driver.current_url}")
            DriverSetup.take_screenshot(driver, name="Registration Page")
            allure.attach(driver.current_url, name="Registration Page URL", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error(f"Failed to navigate to registration page: {e}")
            pytest.fail("Navigation to registration page failed.")

    with allure.step("Fill and submit the registration form"):
        try:
            logger.info("Filling out the registration form.")
            register_page = RegisterPage(driver)
            register_page.enter_name(data["FirstName"], data["LastName"])
            register_page.enter_address(data["Address"], data["City"], data["State"], data["ZipCode"])
            register_page.enter_contact_info(data["Phone"], data["SSN"])
            register_page.enter_username(data["Username"])
            register_page.enter_credentials(data["Password"], data["Confirm"])
            register_page.click_register()
            DriverSetup.take_screenshot(driver, name="Form Submitted")
            logger.info("Registration form submitted successfully.")
        except Exception as e:
            logger.error(f"Error during form submission: {e}")
            DriverSetup.take_screenshot(driver, name="Form Submission Error")
            pytest.fail("Form submission failed.")

    with allure.step("Verify successful registration"):
        try:
            success_message = "Your account was created successfully"
            assert success_message in driver.page_source, "Registration failed!"
            logger.info("Registration completed successfully.")
            DriverSetup.take_screenshot(driver, name="Registration Success")
        except AssertionError:
            logger.error("Registration failed! Success message not found.")
            DriverSetup.take_screenshot(driver, name="Registration Failed")
            pytest.fail("Registration verification failed.")

    logger.info("Registration test completed successfully.")
    allure.attach("Registration test completed successfully.", name="Test Status", attachment_type=allure.attachment_type.TEXT)
