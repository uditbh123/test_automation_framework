import pytest
from pages.login_page import LoginPage
from tests.login_test_data import login_test_data


@pytest.mark.parametrize(
    "username,password,expected_result,expected_message",
    login_test_data
)
def test_login(saucedemo_page, username, password, expected_result, expected_message):
    login_page = LoginPage(saucedemo_page)

    # Single login method handles both valid and invalid flows
    login_page.login(username, password)

    if expected_result:
        assert login_page.is_login_successful(), \
            "Expected successful login but inventory page not reached"
    else:
        assert expected_message in login_page.get_error_message(), \
            f"Expected '{expected_message}' but got '{login_page.get_error_message()}'"