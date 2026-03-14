import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_cart_page_loads(cart_page_ready):
    """After clicking cart icon, cart page should load with title 'Your Cart'."""
    cart = CartPage(cart_page_ready)

    assert cart.is_on_cart_page(), \
        "Not on cart page after clicking cart icon"
    assert cart.get_page_title() == "Your Cart", \
        f"Expected title 'Your Cart' but got '{cart.get_page_title()}'"


def test_added_product_appears_in_cart(cart_page_ready):
    """Product added from inventory should appear in the cart."""
    cart = CartPage(cart_page_ready)

    names = cart.get_cart_item_names()
    assert len(names) > 0, \
        "Cart is empty — expected at least one product"


def test_cart_shows_correct_item_count(cart_page_ready):
    """Cart should show exactly 1 item after adding one product."""
    cart = CartPage(cart_page_ready)

    assert cart.get_cart_item_count() == 1, \
        f"Expected 1 item in cart but found {cart.get_cart_item_count()}"


def test_cart_item_has_valid_price(cart_page_ready):
    """Product price in cart should be a positive number."""
    cart = CartPage(cart_page_ready)

    prices = cart.get_cart_item_prices()
    assert len(prices) > 0, \
        "No prices found in cart"
    assert all(price > 0 for price in prices), \
        f"Expected all prices to be positive but got {prices}"


def test_remove_item_empties_cart(cart_page_ready):
    """Clicking Remove should empty the cart and hide the badge."""
    cart = CartPage(cart_page_ready)

    # Confirm item is there first
    assert cart.get_cart_item_count() == 1, \
        "Expected 1 item before removing"

    cart.remove_first_item()

    # Cart should now be empty
    assert cart.is_cart_empty(), \
        "Cart should be empty after removing the only item"
    assert not cart.is_cart_badge_visible(), \
        "Cart badge should disappear after cart is emptied"


def test_continue_shopping_returns_to_inventory(cart_page_ready):
    """Continue Shopping button should navigate back to inventory page."""
    cart = CartPage(cart_page_ready)

    cart.click_continue_shopping()
    cart_page_ready.wait_for_url("**/inventory.html", timeout=5000)

    assert "inventory" in cart_page_ready.url, \
        "Expected to return to inventory page but URL is: " + cart_page_ready.url


def test_checkout_button_navigates_to_checkout(cart_page_ready):
    """Checkout button should navigate to the checkout information page."""
    cart = CartPage(cart_page_ready)

    cart.click_checkout()
    cart_page_ready.wait_for_url("**/checkout-step-one.html", timeout=5000)

    assert "checkout-step-one" in cart_page_ready.url, \
        "Expected checkout page but URL is: " + cart_page_ready.url