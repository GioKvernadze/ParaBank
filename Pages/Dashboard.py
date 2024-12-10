from Pages.BasePage import BasePage
from Values.pathes import DASHBOARD_NAVIGATION_LOCATORS

class DashboardPage(BasePage):
    def navigate_to_home(self):

        self.wait_for_element_clickable(DASHBOARD_NAVIGATION_LOCATORS["Home"]).click()

    def navigate_to_admin_page(self):

        self.wait_for_element_clickable(DASHBOARD_NAVIGATION_LOCATORS["Admin_Page"]).click()
