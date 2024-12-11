from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_and_click(self, locator):

        element = self.wait_for_element_clickable(locator)
        self.scroll_to_element(element)
        element.click()

    def scroll_and_input(self, locator, value):

        element = self.wait_for_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(value)
