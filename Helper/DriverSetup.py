import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup:
    @staticmethod
    def get_driver(browser="chrome", headless=False):

        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        return driver

    @staticmethod
    def take_screenshot(driver, name="screenshot"):

        try:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
