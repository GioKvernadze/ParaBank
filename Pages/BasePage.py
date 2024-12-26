from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Helper.DriverSetup import DriverSetup

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10, scroll=False):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            if scroll:
                self.scroll_to_element(element)
            element.click()
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Click_Failed")
            raise Exception(f"Element with locator {locator} not clickable within {timeout} seconds.")

    def input_text(self, locator, value, timeout=10, scroll=False):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            if scroll:
                self.scroll_to_element(element)
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Input_Text_Failed")
            raise Exception(f"Input field with locator {locator} not found within {timeout} seconds.")

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            print(f"Failed to scroll to the element: {e}")
            DriverSetup.take_screenshot(self.driver, name="Scroll_Failed")
            raise

    def select_option(self, locator, value=None, index=None, scroll=False, timeout=10):
        try:
            self.wait_for_dropdown_options(locator, timeout)
            element = self.wait_for_element(locator, timeout)
            if element:
                if scroll:
                    self.scroll_to_element(element)
                dropdown = Select(element)
                if value is not None:
                    dropdown.select_by_visible_text(value)
                elif index is not None:
                    dropdown.select_by_index(index)
                else:
                    raise ValueError("Either 'value' or 'index' must be provided to select an option.")
            else:
                raise NoSuchElementException(f"Dropdown with locator {locator} not found!")
        except Exception as e:
            print(f"Error selecting option from dropdown: {e}")
            DriverSetup.take_screenshot(self.driver, name="Select_Option_Failed")
            raise

    def wait_for_dropdown_options(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: len(self.get_dropdown_options(locator, timeout=1)) > 0
            )
            print(f"Dropdown options are loaded for locator {locator}.")
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Dropdown_Options_Load_Failed")
            raise TimeoutException(f"Dropdown options did not load within {timeout} seconds for locator {locator}.")

    def get_dropdown_options(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.driver, timeout).until(lambda driver: len(Select(element).options) > 0)
            dropdown = Select(element)
            options = [option.text for option in dropdown.options]
            print(f"Dropdown options are loaded for locator {locator}: {options}")
            return options
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Get_Options_Failed")
            raise Exception(f"Dropdown with locator {locator} not populated within {timeout} seconds.")

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Element_Not_Found")
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None
