import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_result,expected_message",
    [
        ("standard_user", "secret_sauce", True, None),
        ("invalid_user", "wrong_password", False, "Username and password do not match any user"),
        ("", "", False, "Username is required"),
    ]
)
def test_login(saucedemo_page, username, password, expected_result, expected_message):
    login_page = LoginPage(saucedemo_page)
    login_page.login(username, password)

    if expected_result:
        assert login_page.is_login_successful()
    else:
        assert expected_message in login_page.get_error_message()