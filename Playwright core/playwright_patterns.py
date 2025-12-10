#1. Mẫu test đơn giản theo AAA
# tests/test_login_aaa.py
from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    # Arrange
    page.goto("https://hrm.anhtester.com/erp/login")

    # Act
    page.fill("#iusername", "admin_example")
    page.fill("#ipassword", "123456")
    page.click("button[type='submit']")

    # Assert
    expect(page).to_have_url("https://hrm.anhtester.com/erp/dashboard")
    expect(page.locator("h4.page-title")).to_have_text("Dashboard")


def test_login_wrong_password(page: Page):
    # Arrange
    page.goto("https://hrm.anhtester.com/erp/login")

    # Act
    page.fill("#iusername", "admin_example")
    page.fill("#ipassword", "sai_mat_khau")
    page.click("button[type='submit']")

    # Assert
    expect(page).not_to_have_url("https://hrm.anhtester.com/erp/dashboard")
    expect(page.locator(".alert-danger")).to_be_visible()
#2. Mẫu Page Object cơ bản (Login + Dashboard)
# core/base_page.py
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_and_wait_for_new_page(self, locator: str):
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(locator).click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page
# pages/login_page.py
from playwright.sync_api import Page
from core.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.txt_username = "#iusername"
        self.txt_password = "#ipassword"
        self.btn_login   = "button[type='submit']"

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.txt_username, username)
        self.page.fill(self.txt_password, password)
        self.page.click(self.btn_login)

    def login_with_enter(self, username: str, password: str):
        self.page.fill(self.txt_username, username)
        self.page.fill(self.txt_password, password)
        self.page.keyboard.press("Enter")
# pages/dashboard_page.py
from playwright.sync_api import Page, expect
from core.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.lbl_title = "h4.page-title"
        self.lnk_settings = "a[href$='/erp/settings']"   # chỉnh lại locator đúng trang em

    def assert_is_current_page(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/dashboard")
        expect(self.page.locator(self.lbl_title)).to_have_text("Dashboard")

    def open_settings_in_new_tab(self):
        new_page = self.click_and_wait_for_new_page(self.lnk_settings)
        return new_page    # sẽ wrap bằng SettingsPage ở test hoặc trong factory
#3. Mẫu conftest.py với fixture dashboard_page
# conftest.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    login = LoginPage(page)
    login.open()
    login.login("admin_example", "123456")

    dashboard = DashboardPage(page)
    dashboard.assert_is_current_page()
    return dashboard
#4. Mẫu multi-tab dùng POM
# pages/settings_page.py
from playwright.sync_api import Page, expect
from core.base_page import BasePage

class SettingsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = "h4.page-title"
        self.input_company_name = "input[name='company_name']"
        self.input_logo = "input[type='file'][name='company_logo']"
        self.btn_save = "button[type='submit']"
        self.toast_success = ".toast-message"

    def assert_is_current_page(self):
        expect(self.page.locator(self.heading)).to_have_text("Settings")  # sửa text cho đúng

    def clear_and_set_company_name(self, new_name: str):
        self.page.locator(self.input_company_name).click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Delete")
        self.page.fill(self.input_company_name, new_name)

    def upload_logo(self, file_path: str):
        self.page.set_input_files(self.input_logo, file_path)

    def save(self):
        self.page.click(self.btn_save)

    def assert_update_success(self):
        expect(self.page.locator(self.toast_success)).to_be_visible()
#Test multi-tab:
# tests/test_multi_tab_settings.py
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage

def test_open_settings_in_new_tab(dashboard_page: DashboardPage):
    dashboard = dashboard_page

    # Act: mở tab mới
    settings_raw_page = dashboard.open_settings_in_new_tab()
    settings = SettingsPage(settings_raw_page)

    # Assert
    settings.assert_is_current_page()
    settings_raw_page.close()

    # Quay lại Dashboard
    dashboard.assert_is_current_page()
#5. Mẫu upload file
# tests/test_upload_logo.py
import pathlib
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage

def test_upload_company_logo(dashboard_page: DashboardPage):
    dashboard = dashboard_page

    settings_raw_page = dashboard.open_settings_in_new_tab()
    settings = SettingsPage(settings_raw_page)

    project_root = pathlib.Path(__file__).parents[1]   # lên 1 cấp đến root project
    logo_path = project_root / "data" / "company_logo.png"

    settings.upload_logo(str(logo_path))
    settings.save()
    settings.assert_update_success()
# 6. Mẫu dùng keyboard (Enter + Control+A + Delete)
# tests/test_keyboard_actions.py
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_with_enter(page: Page):
    login = LoginPage(page)
    login.open()
    login.login_with_enter("admin_example", "123456")

    expect(page).to_have_url("https://hrm.anhtester.com/erp/dashboard")


def test_clear_input_with_keyboard(page: Page):
    page.goto("https://hrm.anhtester.com/erp/login")

    username = page.locator("#iusername")
    username.fill("some_text")

    username.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Delete")

    expect(username).to_have_value("")
#7. Mẫu E2E tổng hợp:
# tests/test_e2e_update_company_settings.py
import pathlib
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage

def test_e2e_update_company_settings(dashboard_page: DashboardPage):
    dashboard = dashboard_page

    # Mở Settings tab mới
    settings_raw_page = dashboard.open_settings_in_new_tab()
    settings = SettingsPage(settings_raw_page)

    # Đổi tên công ty
    settings.clear_and_set_company_name("Sun* Vietnam Automation Lab")

    # Upload logo
    project_root = pathlib.Path(__file__).parents[1]
    logo_path = project_root / "data" / "company_logo.png"
    settings.upload_logo(str(logo_path))

    # Lưu
    settings.save()

    # Assert
    settings.assert_update_success()
    settings_raw_page.close()

    # Quay lại Dashboard
    dashboard.assert_is_current_page()

