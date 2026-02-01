import re
import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.sidebar.sidebar_list_item_component import SadebarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SadebarListItemComponent(page, 'logout')
        self.courses_list_item = SadebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SadebarListItemComponent(page, 'dashboard')

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.chek_visible('Logout')
        self.courses_list_item.chek_visible('Courses')
        self.dashboard_list_item.chek_visible('Dashboard')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r'.*/#/auth/login'))
    
    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r'.*/#/courses'))
    
    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r'.*/#/dashboard'))