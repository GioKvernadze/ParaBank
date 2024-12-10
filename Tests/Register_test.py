import pytest
import allure
from Pages.Register import RegisterPage
from Helper.DriverSetup import DriverSetup
from Values.urls import REGISTER_URL
from Values.REGISTER_DATA import register_data

@allure.feature("User Registration")
@allure.story("Register a new user with dynamically generated data")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_new_user(driver):

    with allure.step("Generate user data"):
        # Generate new registration data
        data = register_data(generate_new=True)
        allure.attach(str(data), name="Generated User Data", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Navigate to the registration page"):
        driver.get(REGISTER_URL)
        DriverSetup.take_screenshot(driver, name="Registration Page")
        allure.attach(driver.current_url, name="Registration Page URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Fill and submit the registration form"):
        register_page = RegisterPage(driver)
        register_page.enter_name(data["FirstName"], data["LastName"])
        register_page.enter_address(data["Address"], data["City"], data["State"], data["ZipCode"])
        register_page.enter_contact_info(data["Phone"], data["SSN"])
        register_page.enter_username(data["Username"])
        register_page.enter_credentials(data["Password"], data["Confirm"])
        register_page.click_register()
        DriverSetup.take_screenshot(driver, name="Form Submitted")

    with allure.step("Verify successful registration"):
        success_message = "Your account was created successfully"
        assert success_message in driver.page_source, "Registration failed!"
        DriverSetup.take_screenshot(driver, name="Registration Success")

    allure.attach("Registration test completed successfully.", name="Test Status", attachment_type=allure.attachment_type.TEXT)
