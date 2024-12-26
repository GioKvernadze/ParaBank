import pytest
import allure
from Pages.RegisterPage.Register import RegisterPage
from Values.urls import REGISTER_URL
from Values.register_data import register_data

@allure.feature("User Registration")
@allure.story("Register a new user with dynamically generated data")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_new_user(driver):

    try:
        data = register_data(generate_new=True)
        allure.attach(str(data), name="Generated User Data", attachment_type=allure.attachment_type.TEXT)

        driver.get(REGISTER_URL)
        allure.attach(driver.current_url, name="Registration Page URL", attachment_type=allure.attachment_type.TEXT)

        register_page = RegisterPage(driver)
        register_page.enter_name(data["FirstName"], data["LastName"])
        register_page.enter_address(data["Address"], data["City"], data["State"], data["ZipCode"])
        register_page.enter_contact_info(data["Phone"], data["SSN"])
        register_page.enter_username(data["Username"])
        register_page.enter_credentials(data["Password"], data["Confirm"])
        register_page.click_register()

        success_message = "Your account was created successfully"
        assert success_message in driver.page_source, "Registration failed!"
        allure.attach("Registration test completed successfully.", name="Test Status", attachment_type=allure.attachment_type.TEXT)

    except Exception as e:
        allure.attach(str(e), name="Error Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to error: {e}")
