# Import Page class from Playwright
from playwright.sync_api import Page


class LoginPage:
    """
    Page Object Model for the SauceDemo Login Page.
    Contains all locators and actions related to login functionality.
    """

    def __init__(self, page: Page):
        self.page = page

        # Define locators using Playwright's locator() method
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.inventory_container = page.locator(".inventory_list")

    # -------------------------
    # Action Methods
    # -------------------------

    def enter_username(self, username: str) -> None:
        """Enter username into username field."""
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        """Enter password into password field."""
        self.password_input.fill(password)

    def click_login(self) -> None:
        """Click the login button."""
        self.login_button.click()

    def login(self, username: str, password: str) -> None:
        """
        Perform complete login action.
        This is the business-level method used by tests.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # -------------------------
    # Verification Methods
    # -------------------------

    def is_login_successful(self) -> bool:
        """
        Verify successful login by checking if inventory page is visible.
        """
        return self.inventory_container.is_visible()

    def get_error_message(self) -> str:
        """
        Return error message text for invalid login attempts.
        """
        if self.error_message.is_visible():
            return self.error_message.text_content()
        return ""