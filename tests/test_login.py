from pages.login_page import LoginPage
from utils.screenshot import take_screenshot
import logging

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.login("invalid_user", "wrong_password")

    error_message = login_page.get_error_message
    assert "Username and password do not match" in error_message

def test_locked_user_login(page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")

    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error_message

def test_empty_credentials(page):
    login_page = LoginPage(page)
    login_page.login("", "")

    error_message = login_page.get_error_message()
    assert "Username is required" in error_message

    