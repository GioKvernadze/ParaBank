from Helper.logger import setup_logger
from Pages.Dashboard import DashboardPage
from Helper.DriverSetup import DriverSetup
from Tests.conftest import driver
# Initialize logger
logger = setup_logger()

def test_dashboard_navigation(driver):
    """
    Test navigation from the dashboard to home and admin pages.
    """
    logger.info("Starting the dashboard navigation test.")

    # Initialize the DashboardPage
    dashboard_page = DashboardPage(driver)

    # Navigate to the Home Page
    dashboard_page.navigate_to_home()
    logger.info("Successfully navigated to the Home page.")
    DriverSetup.take_screenshot(driver, "home_page.png")

    # Navigate to the Admin Page
    dashboard_page.navigate_to_admin_page()
    logger.info("Successfully navigated to the Admin page.")
    DriverSetup.take_screenshot(driver, "admin_page.png")
