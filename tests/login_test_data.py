login_test_data = [
    ("standard_user", "secret_sauce", True, None),
    ("invalid_user", "wrong_password", False, "Username and password do not match any user"),
    ("", "", False, "Username is required"),
    ("locked_out_user", "secret_sauce", False, "Sorry, this user has been locked out."),
]