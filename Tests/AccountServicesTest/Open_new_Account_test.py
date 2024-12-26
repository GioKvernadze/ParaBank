import time
import allure
from Pages.AccountServices.OpenNewAccount import OpenNewAccountPage
from Values.account_services_data import account_services_data
from Tests.conftest import *

@allure.feature("Account Services")
@allure.story("Open a New Account")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_user")
def test_open_new_account(driver):

    # Step 1: Load test data
    account_type = account_services_data["ACCOUNT_TYPE"]  # CHECKING or SAVINGS
    from_account_index = account_services_data["FROM_ACCOUNT_INDEX"]

    # Step 2: Perform account creation
    open_new_account_page = OpenNewAccountPage(driver)
    open_new_account_page.navigate_to_open_new_account()
    open_new_account_page.select_account_type(account_type)
    open_new_account_page.select_from_account(from_account_index)
    open_new_account_page.click_open_new_account()

    # Step 3: Verify account creation success
    account_number = open_new_account_page.verify_account_created()
    assert account_number is not None, "Failed to create a new account!"
