import pytest
import allure
from Values.urls import REGISTER_URL
from Pages.Register import RegisterPage
from Values.REGISTER_DATA import register_data
from Helper.DriverSetup import DriverSetup

@allure.feature("User Registration")
@allure.story("Register a new user")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_new_user(driver):
    """
    Test registration with dynamically generated data.
    """
    with allure.step("Generate user data"):
        data = register_data(generate_new=True)

    with allure.step("Navigate to the registration page"):
        driver.get(REGISTER_URL)
        DriverSetup.take_screenshot(driver, name="Registration Page")

    with allure.step("Fill and submit the registration form"):
        register_page = RegisterPage(driver)
        register_page.enter_name(data["FirstName"], data["LastName"])
        register_page.enter_address(data["Address"], data["City"], data["State"], data["ZipCode"])
        register_page.enter_contact_info(data["Phone"], data["SSN"])
        register_page.enter_username(data["Username"])
        register_page.enter_credentials(data["Password"], data["Confirm"])
        DriverSetup.take_screenshot(driver, name="Form Submitted")
        register_page.click_register()


    with allure.step("Verify registration success"):
        assert "Your account was created successfully" in driver.page_source, "Registration failed!"
        DriverSetup.take_screenshot(driver, name="Registration Success")
