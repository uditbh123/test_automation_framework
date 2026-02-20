from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot

def test_valid_login():
    with sync_playwright() as p:

        browser = p.chromium.lauch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com")

        login = LoginPage(page)

        login.login(
            username="standard_user",
            password="secret_sauce"
        )

        try:
            assert "inventory" in page.url

        except AssertionError:

            take_screenshot(page, "valid_login_failed")

            raise 

        finally:
            browser.close()