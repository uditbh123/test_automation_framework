import pytest
from pages.login_page import LoginPage
from tests.test_data_login import login_test_data


@pytest.mark.parametrize(
    "username,password,expected_result,expected_message",
    login_test_data
)
def test_login(saucedemo_page, username, password, expected_result, expected_message):
    login_page = LoginPage(saucedemo_page)

    # Decide which login method to use based on expected_result
    if expected_result:
        # valid login, page navigates
        login_page.login_with_navigation(username, password)
        assert login_page.is_login_successful()
    else:
        # invalid login, page stays
        login_page.login_without_navigation(username, password)
        assert expected_message in login_page.get_error_message()