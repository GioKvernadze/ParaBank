import pytest
import allure
from Pages.AdminPage.Admin import AdminPage
from Values.admin_data import admin_data

@allure.feature("Admin Page")
@allure.story("Perform Admin Actions and Update Application Settings")
@pytest.mark.usefixtures("login_user")
def test_admin_page_actions(driver):

    # Step 1: Retrieve admin data
    data = admin_data()

    # Step 2: Perform admin actions
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin_page()
    assert admin_page.verify_admin_page_loaded(), "Admin Page did not load!"

    admin_page.initialize_database()
    admin_page.clean_database()
    admin_page.shutdown_jms_service()
    admin_page.update_application_settings(
        initial_balance=data["INITIAL_BALANCE"],
        minimum_balance=data["MINIMUM_BALANCE"]
    )

    # Step 3: Verify successful update
    assert admin_page.verify_admin_page_loaded(), "Admin Page verification failed!"
