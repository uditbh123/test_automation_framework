import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_purchase_journey(saucedemo_page):
    """
    End-to-End test covering the complete user journey:
    Login → Inventory → Add to Cart → Cart → Checkout → Order Confirmation

    This test verifies the entire system works together as a real user
    would experience it — no fixtures doing setup, no isolation.
    Every step depends on the previous one succeeding.
    """

    # -------------------------------------------------------
    # STEP 1 — Login
    # -------------------------------------------------------
    login_page = LoginPage(saucedemo_page)
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_login_successful(), \
        "STEP 1 FAILED: Could not log in as standard_user"

    print("\n✅ Step 1 passed — Logged in successfully")

    # -------------------------------------------------------
    # STEP 2 — Inventory: sort by price and capture cheapest product
    # -------------------------------------------------------
    inventory = InventoryPage(saucedemo_page)

    assert inventory.is_on_inventory_page(), \
        "STEP 2 FAILED: Not on inventory page after login"

    # Sort by price low to high so first product is the cheapest
    inventory.sort_by("lohi")

    # Capture the name and price of the first (cheapest) product
    all_names  = inventory.get_all_product_names()
    all_prices = inventory.get_all_product_prices()

    cheapest_product_name  = all_names[0]
    cheapest_product_price = all_prices[0]

    assert cheapest_product_name != "", \
        "STEP 2 FAILED: Could not read product name from inventory"
    assert cheapest_product_price > 0, \
        "STEP 2 FAILED: Product price should be greater than zero"

    print(f"✅ Step 2 passed — Cheapest product: '{cheapest_product_name}' at ${cheapest_product_price}")

    # -------------------------------------------------------
    # STEP 3 — Add cheapest product to cart
    # -------------------------------------------------------
    inventory.add_first_product_to_cart()

    cart_count = inventory.get_cart_count()
    assert cart_count == 1, \
        f"STEP 3 FAILED: Expected cart count 1 but got {cart_count}"

    print(f"✅ Step 3 passed — Product added to cart, badge shows {cart_count}")

    # -------------------------------------------------------
    # STEP 4 — Navigate to cart and verify correct product
    # -------------------------------------------------------
    saucedemo_page.click(".shopping_cart_link")
    saucedemo_page.wait_for_url("**/cart.html", timeout=5000)

    cart = CartPage(saucedemo_page)

    assert cart.is_on_cart_page(), \
        "STEP 4 FAILED: Not on cart page after clicking cart icon"

    cart_names  = cart.get_cart_item_names()
    cart_prices = cart.get_cart_item_prices()

    assert cheapest_product_name in cart_names, \
        f"STEP 4 FAILED: Expected '{cheapest_product_name}' in cart but found {cart_names}"

    assert cheapest_product_price in cart_prices, \
        f"STEP 4 FAILED: Expected price ${cheapest_product_price} in cart but found {cart_prices}"

    print(f"✅ Step 4 passed — Correct product and price verified in cart")

    # -------------------------------------------------------
    # STEP 5 — Proceed to checkout and fill in information
    # -------------------------------------------------------
    cart.click_checkout()
    saucedemo_page.wait_for_url("**/checkout-step-one.html", timeout=5000)

    checkout = CheckoutPage(saucedemo_page)

    assert checkout.is_on_step_one(), \
        "STEP 5 FAILED: Not on checkout step 1"

    checkout.enter_information("John", "Doe", "12345")
    checkout.click_continue()
    saucedemo_page.wait_for_url("**/checkout-step-two.html", timeout=5000)

    assert checkout.is_on_step_two(), \
        "STEP 5 FAILED: Did not reach checkout step 2 after filling in information"

    print("✅ Step 5 passed — Checkout information filled, on step 2")

    # -------------------------------------------------------
    # STEP 6 — Verify order summary and price calculation
    # -------------------------------------------------------
    summary_names = checkout.get_summary_item_names()

    assert cheapest_product_name in summary_names, \
        f"STEP 6 FAILED: Expected '{cheapest_product_name}' in summary but found {summary_names}"

    item_total = checkout.get_item_total()
    tax        = checkout.get_tax()
    total      = checkout.get_total()

    expected_total = round(item_total + tax, 2)
    assert round(total, 2) == expected_total, \
        f"STEP 6 FAILED: Expected total {expected_total} but got {total}"

    assert item_total == cheapest_product_price, \
        f"STEP 6 FAILED: Item total ${item_total} doesn't match inventory price ${cheapest_product_price}"

    print(f"✅ Step 6 passed — Order summary correct. Item: ${item_total}, Tax: ${tax}, Total: ${total}")

    # -------------------------------------------------------
    # STEP 7 — Complete the order and verify confirmation
    # -------------------------------------------------------
    checkout.click_finish()
    saucedemo_page.wait_for_url("**/checkout-complete.html", timeout=5000)

    assert checkout.is_on_confirmation_page(), \
        "STEP 7 FAILED: Not on confirmation page after clicking Finish"

    confirmation = checkout.get_confirmation_message()
    assert confirmation == "Thank you for your order!", \
        f"STEP 7 FAILED: Unexpected confirmation message: '{confirmation}'"

    print(f"✅ Step 7 passed — Order complete! '{confirmation}'")
    print("\n🎉 FULL E2E JOURNEY PASSED — Login → Inventory → Cart → Checkout → Confirmation")