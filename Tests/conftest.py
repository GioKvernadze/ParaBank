import pytest
from Helper.DriverSetup import DriverSetup
from Helper.LoginHelper import LoginHelper



@pytest.fixture(scope="session")
def driver():

    print("Starting WebDriver...")
    driver = DriverSetup.get_driver(browser="chrome", headless=False)
    yield driver  # Provide the driver instance to the tests
    print("Closing WebDriver...")
    driver.quit()


@pytest.fixture(scope="session")
def login_user(driver):

    login_helper = LoginHelper(driver)
    try:
        login_helper.login_with_fallback()
        print("Login fixture completed successfully.")
    except Exception as e:
        pytest.fail(f"Login fixture failed: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        from Helper.DriverSetup import DriverSetup
        DriverSetup.take_screenshot(driver, name=f"Failure_{item.name}")
