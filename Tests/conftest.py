import pytest
from Helper.DriverSetup import DriverSetup
from Values.urls import BASE_URL
from Pages.Login import LoginPage
from Values.REGISTER_DATA import register_data

@pytest.fixture(scope="session")
def driver():

    print("Starting WebDriver...")
    driver = DriverSetup.get_driver(browser="chrome", headless=False)
    yield driver  # Provide the driver instance to the tests
    print("Closing WebDriver...")
    driver.quit()

@pytest.fixture(scope="session")
def login_user(driver):

    print("Logging in to maintain session...")
    # Retrieve credentials
    data = register_data()
    username = data["Username"]
    password = data["Password"]

    # Navigate to the login page and log in
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Verify login
    assert "Accounts Overview" in driver.page_source, "Login precondition failed!"
    print("User successfully logged in.")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Take a screenshot on test failure
    if report.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        DriverSetup.take_screenshot(driver, name=f"Failure_{item.name}")
