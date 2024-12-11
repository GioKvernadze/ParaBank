from selenium.webdriver.common.by import By

REGISTER_PAGE_LOCATORS = {
    "FIRST_NAME_FIELD": (By.ID, "customer.firstName"),
    "LAST_NAME_FIELD": (By.ID, "customer.lastName"),
    "ADDRESS_FIELD": (By.ID, "customer.address.street"),
    "CITY_FIELD": (By.ID, "customer.address.city"),
    "STATE_FIELD": (By.ID, "customer.address.state"),
    "ZIP_CODE_FIELD": (By.ID, "customer.address.zipCode"),
    "PHONE_FIELD": (By.ID, "customer.phoneNumber"),
    "SSN_FIELD": (By.ID, "customer.ssn"),
    "USERNAME_FIELD": (By.ID, "customer.username"),
    "PASSWORD_FIELD": (By.ID, "customer.password"),
    "CONFIRM_PASSWORD_FIELD": (By.ID, "repeatedPassword"),
    "REGISTER_BUTTON": (By.XPATH, "//input[@value='Register']")
}
LOGIN_PAGE_LOCATORS = {
    "USERNAME_FIELD": (By.NAME, "username"),
    "PASSWORD_FIELD": (By.NAME, "password"),
    "LOGIN_BUTTON": (By.CSS_SELECTOR, "input.button[value='Log In']"),
}

ADMIN_LOCATORS = {
    "ADMIN_BUTTON": (By.LINK_TEXT, "Admin Page"),
    "ADMIN_HEADER": (By.XPATH, "//h1[contains(text(),'Administration')]"),
    "INIT_BUTTON": (By.XPATH, "//button[@name='action' and @value='INIT']"),
    "CLEAN_BUTTON": (By.XPATH, "//button[@name='action' and @value='CLEAN']"),
    "SHUTDOWN_JMS_BUTTON": (By.XPATH, "//input[@value='Shutdown']"),
    "INITIAL_BALANCE": (By.ID, "initialBalance"),
    "MINIMUM_BALANCE": (By.ID, "minimumBalance"),
    "SUBMIT_BUTTON": (By.XPATH, "//input[@type='submit' and @class='button']"),
}
