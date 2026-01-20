import re
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.sidebar.sidebar_list_item_component import SadebarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SadebarListItemComponent(page, 'logout')
        self.courses_list_item = SadebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SadebarListItemComponent(page, 'dashboard')

    def chek_visible(self):
        self.logout_list_item.chek_visible('Logout')
        self.courses_list_item.chek_visible('Courses')
        self.dashboard_list_item.chek_visible('Dashboard')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r'*/#/auth/login'))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r'*/#/courses'))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r'*/#/dashboard'))