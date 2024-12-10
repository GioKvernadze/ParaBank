import pytest
from Helper.DriverSetup import DriverSetup

@pytest.fixture(scope="session")
def driver():
    """
    Pytest fixture to set up and tear down the WebDriver for the entire session.
    """
    print("Starting WebDriver...")
    driver = DriverSetup.get_driver(browser="chrome", headless=False)
    yield driver  # Provide the driver instance to the tests
    print("Closing WebDriver...")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot when a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    # Take a screenshot on test failure
    if report.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        DriverSetup.take_screenshot(driver, name=f"Failure_{item.name}")
