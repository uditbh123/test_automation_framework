from pages.login_page import LoginPage
from utils.screenshot import take_screenshot
import logging

def test_valid_login(page):
    logging.info("Navigating to SauceDemo website")
    page.goto("https://www.saucedemo.com")

    login = LoginPage(page)
    logging.info("Performing login action")
    login.login(username="standard_user", password="secret_sauce")

    try:
        assert "inventory" in page.url
        logging.info("Login successful")
    except AssertionError:
        logging.error("Login failed, taking screenshot")
        take_screenshot(page, "valid_login_failed")
        raise