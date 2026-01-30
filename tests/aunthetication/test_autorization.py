import pytest
from pages.aunthetication.login_page import LoginPage
from pages.aunthetication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAutorization:
    def test_navigate_from_autorization_to_registration(self, registration_page: RegistrationPage, login_page: LoginPage):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(
            email='', 
            username='', 
            password=''
            )
        
    def test_successfull_autorization(
            self, 
            registration_page: RegistrationPage, 
            dashboard_page: DashboardPage,
            login_page: LoginPage
            ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill_form(
            email="user.name@gmail.com",
            password="password",
            username="username")
        registration_page.click_registratio_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()
        login_page.login_form.fill_form(
            email="user.name@gmail.com",
            password="password")
        login_page.click_login_button()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

    @pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"), 
        ("user.name@gmail.com", "  "),
        ("  ", "password")
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill_form(email = email, password = password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()
        
    