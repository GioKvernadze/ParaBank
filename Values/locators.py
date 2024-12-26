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
    "SUCCESS_MESSAGE": (By.XPATH, "//p[contains(text(), 'Settings saved successfully')]"),
    "SUBMIT_BUTTON": (By.XPATH, "//input[@value='Submit']")

}

ACCOUNT_SERVICES_LOCATORS = {
    "OPEN_NEW_ACCOUNT": ("XPATH", "//a[contains(@href, 'openaccount.htm')]"),
    "ACCOUNTS_OVERVIEW": ("XPATH", "//a[contains(@href, 'overview.htm')]"),
    "TRANSFER_FUNDS": ("XPATH", "//a[contains(@href, 'transfer.htm')]"),
    "BILL_PAY": ("XPATH", "//a[contains(@href, 'billpay.htm')]"),
    "FIND_TRANSACTIONS": ("XPATH", "//a[contains(@href, 'findtrans.htm')]"),
    "UPDATE_CONTACT_INFO": ("XPATH", "//a[contains(@href, 'updateprofile.htm')]"),
    "REQUEST_LOAN": ("XPATH", "//a[contains(@href, 'requestloan.htm')]"),
    "LOG_OUT": ("XPATH", "//a[contains(@href, 'logout.htm')]"),
}

OPEN_NEW_ACCOUNT_LOCATORS = {
    "OPEN_NEW_ACCOUNT": (By.XPATH, "//a[contains(@href, 'openaccount.htm')]"),
    "ACCOUNT_TYPE_DROPDOWN": (By.XPATH, "//select[@id='type' and @class='input']"),
    "FROM_ACCOUNT_DROPDOWN": (By.ID, "fromAccountId"),
    "OPEN_NEW_ACCOUNT_BUTTON": (By.XPATH, "//input[@value='Open New Account']"),
    "ACCOUNT_OPENED_MESSAGE": (By.XPATH, "//h1[contains(text(), 'Account Opened')]"),
    "NEW_ACCOUNT_NUMBER": (By.ID, "newAccountId"),
}
