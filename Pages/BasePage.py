from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from Helper.DriverSetup import DriverSetup  # Import the existing take_screenshot method


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # --- Wait Methods ---
    def wait_for_element(self, locator, timeout=10):
        """
        Waits for an element to be present in the DOM and returns it.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Element_Not_Found")
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None

    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Waits for an element to be clickable and returns it.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            DriverSetup.take_screenshot(self.driver, name="Element_Not_Clickable")
            print(f"Element with locator {locator} not clickable within {timeout} seconds.")
            return None

    # --- Scroll Methods ---
    def scroll_and_input(self, locator, value):
        """
        Scrolls to an element and inputs text.
        """
        element = self.wait_for_element(locator)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
            element.clear()
            element.send_keys(value)
            DriverSetup.take_screenshot(self.driver, name="Scrolled_And_Inputted_Value")
        else:
            print(f"Input field with locator {locator} not found!")
            DriverSetup.take_screenshot(self.driver, name="Input_Field_Not_Found")

    def scroll_and_select(self, locator, value):
        """
        Scrolls to a dropdown and selects an option by visible text.
        """
        element = self.wait_for_element(locator)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
            dropdown = Select(element)
            dropdown.select_by_visible_text(value)
            DriverSetup.take_screenshot(self.driver, name="Scrolled_And_Selected_Element")

        else:
            print(f"Dropdown with locator {locator} not found!")
            DriverSetup.take_screenshot(self.driver, name="Dropdown_Not_Found")

    def select(self, locator, value=None, index=None):
        """
        Select an option in a dropdown by visible text or index.
        """
        element = self.wait_for_element(locator)
        if element:
            dropdown = Select(element)
            if value is not None:
                dropdown.select_by_visible_text(value)
            elif index is not None:
                dropdown.select_by_index(index)
            else:
                raise ValueError("Either 'value' or 'index' must be provided to select an option.")
        else:
            raise Exception(f"Dropdown with locator {locator} not found!")

    def get_dropdown_options(self, locator):
        """
        Retrieves all options from a dropdown.
        """
        element = self.wait_for_element(locator)
        if element:
            dropdown = Select(element)
            return [option.text for option in dropdown.options]
        else:
            print(f"Dropdown with locator {locator} not found!")
            DriverSetup.take_screenshot(self.driver, name="Dropdown_Not_Found")
            return []
