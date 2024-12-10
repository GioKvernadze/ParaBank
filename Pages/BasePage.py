from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default wait time of 10 seconds

    def wait_for_element(self, locator):

        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"ERROR: Element with locator {locator} was not visible within the timeout period.")
            return None

    def wait_for_element_clickable(self, locator):

        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"ERROR: Element with locator {locator} was not clickable within the timeout period.")
            return None
