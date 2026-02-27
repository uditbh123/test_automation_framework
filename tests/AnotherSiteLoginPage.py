from playwright.sync_api import Page

class AnotherSiteLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#email")
        self.password_input = page.locator("#pass")
        self.login_button = page.locator(".login-btn")
        self.error_message = page.locator(".error-msg")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content() if self.error_message.is_visible() else ""
    