import pytest
import allure
from Values.urls import BASE_URL
from Pages.Login import LoginPage
from Values.REGISTER_DATA import register_data
from Helper.DriverSetup import DriverSetup

@allure.feature("User Login")
@allure.story("Login with existing user credentials")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_existing_user(driver):

    with allure.step("Retrieve user credentials from saved data"):
        data = register_data()
        username = data["Username"]
        password = data["Password"]
        allure.attach(f"Username: {username}\nPassword: {password}", name="Login Credentials", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Navigate to the login page"):
        driver.get(BASE_URL)
        DriverSetup.take_screenshot(driver, name="Login Page")
        allure.attach(driver.current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Enter login credentials"):
        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        DriverSetup.take_screenshot(driver, name="Credentials Entered")

    with allure.step("Submit login form"):
        login_page.click_login()
        DriverSetup.take_screenshot(driver, name="After Submit")

    with allure.step("Verify successful login"):
        success_message = "Accounts Overview"
        assert success_message in driver.page_source, "Login failed!"
        DriverSetup.take_screenshot(driver, name="Login Success")
        allure.attach(driver.page_source, name="Page Source", attachment_type=allure.attachment_type.TEXT)
