import pytest
from pages.checkout_page import CheckoutPage


def test_checkout_page_loads(checkout_ready):
    """After clicking checkout from cart, step 1 should load correctly."""
    checkout = CheckoutPage(checkout_ready)

    assert checkout.is_on_step_one(), \
        "Expected to be on checkout step 1 but URL is: " + checkout_ready.url
    assert checkout.get_page_title() == "Checkout: Your Information", \
        f"Unexpected page title: '{checkout.get_page_title()}'"


def test_empty_fields_shows_error(checkout_ready):
    """Clicking Continue with empty fields should show an error message."""
    checkout = CheckoutPage(checkout_ready)

    checkout.click_continue()

    error = checkout.get_error_message()
    assert error != "", \
        "Expected an error message but none appeared"
    assert "First Name is required" in error, \
        f"Unexpected error message: '{error}'"


def test_missing_last_name_shows_error(checkout_ready):
    """Filling first name and zip but not last name should show specific error."""
    checkout = CheckoutPage(checkout_ready)

    checkout.enter_information("John", "", "12345")
    checkout.click_continue()

    error = checkout.get_error_message()
    assert "Last Name is required" in error, \
        f"Expected last name error but got: '{error}'"


def test_valid_info_proceeds_to_step_two(checkout_ready):
    """Filling all fields correctly should navigate to checkout step 2."""
    checkout = CheckoutPage(checkout_ready)

    checkout.enter_information("John", "Doe", "12345")
    checkout.click_continue()
    checkout_ready.wait_for_url("**/checkout-step-two.html", timeout=5000)

    assert checkout.is_on_step_two(), \
        "Expected checkout step 2 but URL is: " + checkout_ready.url


def test_order_summary_shows_correct_item(checkout_ready):
    """Step 2 should show the product that was added to cart."""
    checkout = CheckoutPage(checkout_ready)

    # Navigate to step 2
    checkout.enter_information("John", "Doe", "12345")
    checkout.click_continue()
    checkout_ready.wait_for_url("**/checkout-step-two.html", timeout=5000)

    item_names = checkout.get_summary_item_names()
    assert len(item_names) > 0, \
        "No items found in order summary"


def test_price_total_is_correct(checkout_ready):
    """Total price on step 2 should equal item total + tax."""
    checkout = CheckoutPage(checkout_ready)

    # Navigate to step 2
    checkout.enter_information("John", "Doe", "12345")
    checkout.click_continue()
    checkout_ready.wait_for_url("**/checkout-step-two.html", timeout=5000)

    item_total = checkout.get_item_total()
    tax        = checkout.get_tax()
    total      = checkout.get_total()

    # Round to 2 decimal places to avoid floating point issues
    expected_total = round(item_total + tax, 2)
    assert round(total, 2) == expected_total, \
        f"Expected total {expected_total} but got {total}"


def test_finish_completes_order(checkout_ready):
    """Clicking Finish on step 2 should land on the confirmation page."""
    checkout = CheckoutPage(checkout_ready)

    # Navigate through step 1 to step 2
    checkout.enter_information("John", "Doe", "12345")
    checkout.click_continue()
    checkout_ready.wait_for_url("**/checkout-step-two.html", timeout=5000)

    checkout.click_finish()
    checkout_ready.wait_for_url("**/checkout-complete.html", timeout=5000)

    assert checkout.is_on_confirmation_page(), \
        "Expected confirmation page but URL is: " + checkout_ready.url
    assert checkout.get_confirmation_message() == "Thank you for your order!", \
        f"Unexpected confirmation message: '{checkout.get_confirmation_message()}'"


def test_cancel_returns_to_cart(checkout_ready):
    """Clicking Cancel on step 1 should return to the cart page."""
    checkout = CheckoutPage(checkout_ready)

    checkout.click_cancel()
    checkout_ready.wait_for_url("**/cart.html", timeout=5000)

    assert "cart" in checkout_ready.url, \
        "Expected cart page but URL is: " + checkout_ready.url