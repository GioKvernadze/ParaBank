import pytest
import allure
from Pages.Admin import AdminPage
from Helper.DriverSetup import DriverSetup
from Helper.logger import setup_logger
from Values.ADMIN_DATA import admin_data

# Initialize logger
logger = setup_logger()

@allure.feature("Admin Page")
@allure.story("Perform Admin Actions and Update Application Settings")
@pytest.mark.usefixtures("login_user")
def test_admin_page_actions(driver):
    with allure.step("Retrieve admin configuration data"):
        try:
            logger.info("Retrieving admin configuration data.")
            data = admin_data()
            logger.info(f"Admin configuration data: {data}")
        except Exception as e:
            logger.error(f"Failed to retrieve admin data: {e}")
            pytest.fail("Could not load admin configuration data.")

    with allure.step("Navigate to the Admin Page"):
        try:
            logger.info("Navigating to the Admin Page.")
            admin_page = AdminPage(driver)
            admin_page.navigate_to_admin_page()
            assert admin_page.verify_admin_page_loaded(), "Admin Page did not load!"
            logger.info("Admin Page loaded successfully.")
            DriverSetup.take_screenshot(driver, "Admin_Page_Loaded")
        except Exception as e:
            logger.error(f"Error while navigating to Admin Page: {e}")
            DriverSetup.take_screenshot(driver, "Admin_Page_Navigation_Failed")
            pytest.fail("Failed to load Admin Page.")

    with allure.step("Initialize the Database"):
        try:
            logger.info("Initializing the database.")
            admin_page.initialize_database()
            DriverSetup.take_screenshot(driver, "Database_Initialized")
            logger.info("Database initialized successfully.")
        except Exception as e:
            logger.error(f"Error while initializing the database: {e}")
            DriverSetup.take_screenshot(driver, "Database_Initialization_Failed")
            pytest.fail("Database initialization failed.")

    with allure.step("Clean the Database"):
        try:
            logger.info("Cleaning the database.")
            admin_page.clean_database()
            DriverSetup.take_screenshot(driver, "Database_Cleaned")
            logger.info("Database cleaned successfully.")
        except Exception as e:
            logger.error(f"Error while cleaning the database: {e}")
            DriverSetup.take_screenshot(driver, "Database_Cleanup_Failed")
            pytest.fail("Database cleanup failed.")

    with allure.step("Shutdown the JMS Service"):
        try:
            logger.info("Shutting down JMS service.")
            admin_page.shutdown_jms_service()
            DriverSetup.take_screenshot(driver, "JMS_Service_Shutdown")
            logger.info("JMS service shutdown successfully.")
        except Exception as e:
            logger.error(f"Error while shutting down JMS service: {e}")
            DriverSetup.take_screenshot(driver, "JMS_Service_Shutdown_Failed")
            pytest.fail("JMS service shutdown failed.")

    with allure.step("Update Application Settings"):
        try:
            logger.info("Updating application settings.")
            admin_page.update_application_settings(
                initial_balance=data["INITIAL_BALANCE"],
                minimum_balance=data["MINIMUM_BALANCE"]
            )
            DriverSetup.take_screenshot(driver, "Application_Settings_Updated")
            logger.info("Application settings updated successfully.")
        except Exception as e:
            logger.error(f"Error while updating application settings: {e}")
            DriverSetup.take_screenshot(driver, "Application_Settings_Update_Failed")
            pytest.fail("Application settings update failed.")

    with allure.step("Verify Admin Page Loaded Again"):
        try:
            logger.info("Verifying Admin Page is still loaded.")
            assert admin_page.verify_admin_page_loaded(), "Admin Page verification failed!"
            DriverSetup.take_screenshot(driver, "Admin_Page_Verified")
            logger.info("Admin Page verification successful.")
        except AssertionError:
            logger.error("Admin Page verification failed!")
            DriverSetup.take_screenshot(driver, "Admin_Page_Verification_Failed")
            pytest.fail("Admin Page verification failed.")
        except Exception as e:
            logger.error(f"Unexpected error during Admin Page verification: {e}")
            pytest.fail("Unexpected error during Admin Page verification.")

    logger.info("Test for Admin Page actions completed successfully.")
