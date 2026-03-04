from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.inventory_container = page.locator(".inventory_list")

    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login(self) -> None:
        self.login_button.click()

    def login(self, username: str, password: str) -> None:
        """Single login method — handles both valid and invalid flows."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self) -> bool:
        try:
            self.page.wait_for_url("**/inventory.html", timeout=3000)
            return self.inventory_container.is_visible()
        except PlaywrightTimeoutError:
            return False

    def get_error_message(self) -> str:
        try:
            self.error_message.wait_for(state="visible", timeout=2000)
            return self.error_message.text_content().strip()
        except PlaywrightTimeoutError:
            return ""