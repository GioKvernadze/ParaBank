import pytest
import allure
from Pages.AccountServices.OpenNewAccount import OpenNewAccountPage
from Helper.DriverSetup import DriverSetup
from Values.ACCOUNT_SERVICES_DATA import ACCOUNT_SERVICES_DATA
from Helper.logger import setup_logger

# Initialize logger
logger = setup_logger()

@allure.feature("Account Services")
@allure.story("Open a New Account")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login_user")
def test_open_new_account(driver):
    """
    Test for opening a new account with specified account type and source account.
    """
    # Load test data
    try:
        logger.info("Loading test data for 'Open New Account'.")
        account_type = ACCOUNT_SERVICES_DATA["ACCOUNT_TYPE"]  # CHECKING or SAVINGS
        from_account_index = ACCOUNT_SERVICES_DATA["FROM_ACCOUNT_INDEX"]
        logger.info(f"Account Type: {account_type}, From Account Index: {from_account_index}")
    except KeyError as e:
        logger.error(f"Missing test data key: {e}")
        pytest.fail(f"Test data error: {e}")

    with allure.step("Navigate to 'Open New Account' page"):
        try:
            logger.info("Navigating to 'Open New Account' page.")
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.navigate_to_open_new_account()
            DriverSetup.take_screenshot(driver, "Navigate_Open_New_Account")
        except Exception as e:
            logger.error(f"Error navigating to 'Open New Account' page: {e}")
            DriverSetup.take_screenshot(driver, "Navigation_Failed")
            pytest.fail("Failed to navigate to 'Open New Account' page.")

    with allure.step("Fill in the 'Open New Account' form"):
        try:
            logger.info("Filling in 'Open New Account' form.")
            open_new_account_page.select_account_type(account_type)
            open_new_account_page.select_from_account(from_account_index)
            open_new_account_page.click_open_new_account()
            DriverSetup.take_screenshot(driver, "Form_Filled")
        except Exception as e:
            logger.error(f"Error filling the 'Open New Account' form: {e}")
            DriverSetup.take_screenshot(driver, "Form_Fill_Failed")
            pytest.fail("Failed to fill 'Open New Account' form.")

    with allure.step("Verify account creation success"):
        try:
            logger.info("Verifying account creation success.")
            account_number = open_new_account_page.verify_account_created()
            assert account_number is not None, "Failed to create a new account!"
            logger.info(f"New account created successfully: {account_number}")
            allure.attach(account_number, name="New Account Number", attachment_type=allure.attachment_type.TEXT)
            DriverSetup.take_screenshot(driver, "Account_Created")
        except AssertionError:
            logger.error("New account creation failed.")
            DriverSetup.take_screenshot(driver, "Account_Creation_Failed")
            pytest.fail("New account creation failed.")
        except Exception as e:
            logger.error(f"Unexpected error during account creation verification: {e}")
            DriverSetup.take_screenshot(driver, "Verification_Failed")
            pytest.fail("Unexpected error during account creation verification.")

    logger.info("Test for 'Open New Account' completed successfully.")
