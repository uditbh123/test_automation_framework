# login_page.py
from playwright.sync_api import Page


class LoginPage:
    """
    Page Object Model for the SauceDemo Login Page.
    Handles valid and invalid login flows safely.
    """

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.inventory_container = page.locator(".inventory_list")

    # -------------------------
    # Action Methods
    # -------------------------

    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login(self) -> None:
        self.login_button.click()

    # -------------------------
    # Login Methods
    # -------------------------

    def login_with_navigation(self, username: str, password: str) -> None:
        """
        Use this for valid login where page navigates to inventory.
        """
        self.enter_username(username)
        self.enter_password(password)
        with self.page.expect_navigation():
            self.click_login()

    def login_without_navigation(self, username: str, password: str) -> None:
        """
        Use this for invalid login or empty credentials.
        Waits shortly for error message to appear.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        # Wait for error message to appear
        try:
            self.error_message.wait_for(state="visible", timeout=2000)
        except:
            pass

    # -------------------------
    # Verification Methods
    # -------------------------

    def is_login_successful(self) -> bool:
        """
        Checks if URL contains 'inventory' and inventory container is visible.
        """
        return "inventory" in self.page.url and self.inventory_container.is_visible()

    def get_error_message(self) -> str:
        """
        Returns error message text safely, or empty string if not visible.
        """
        if self.error_message.is_visible():
            return self.error_message.text_content().strip()
        return ""