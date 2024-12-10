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
    "USERNAME_FIELD": (By.NAME, "username"),  # Locate by 'name' attribute
    "PASSWORD_FIELD": (By.NAME, "password"),  # Locate by 'name' attribute
    "LOGIN_BUTTON": (By.CSS_SELECTOR, "input.button[value='Log In']"),  # Locate by CSS
}

DASHBOARD_NAVIGATION_LOCATORS = {
    "Home": (By.LINK_TEXT, "home"),
    "Admin_Page": (By.LINK_TEXT, "Admin Page"),
}
