from pages.login_page import LoginPage

def test_valid_login(saucedemo_page):
    login_page = LoginPage(saucedemo_page)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful()

def test_invalid_login(saucedemo_page):
    login_page = LoginPage(saucedemo_page)
    login_page.login("invalid_user", "wrong_password")
    assert "Username and password do not match any user" in login_page.get_error_message()

def test_empty_credentials(saucedemo_page):
    login_page = LoginPage(saucedemo_page)
    login_page.login("", "")
    assert "Username is required" in login_page.get_error_message()