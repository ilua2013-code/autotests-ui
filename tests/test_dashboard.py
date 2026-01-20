from pages.dashboard_page import DashboardPage
import pytest

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.navbar.chek_visible('username')
    dashboard_page_with_state.chek_visable_dashboard_title()
    dashboard_page_with_state.chek_visable_scores_chart()
    dashboard_page_with_state.chek_visable_courses_chart()
    dashboard_page_with_state.chek_visable_students_chart()
    dashboard_page_with_state.check_visible_activities_chart()