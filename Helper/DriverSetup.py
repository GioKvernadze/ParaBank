import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Fixture to set up and tear down the WebDriver for each test.
    """
    print("Starting test setup...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver  # Provide the WebDriver instance to the test
    print("Cleaning up after test...")
    driver.quit()

