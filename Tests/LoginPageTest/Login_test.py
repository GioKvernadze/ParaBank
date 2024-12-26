import allure
from Pages.LoginPage.Login import LoginPage
from Values.urls import BASE_URL
from Values.register_data import register_data

@allure.feature("User Login")
@allure.story("Verify Login Functionality")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_functionality(driver):

    # Step 1: Retrieve credentials
    data = register_data()
    username = data["Username"]
    password = data["Password"]

    # Step 2: Perform login
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Step 3: Verify login success
    assert "Accounts Overview" in driver.page_source, "Login verification failed!"
