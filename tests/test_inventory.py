import pytest
from pages.inventory_page import InventoryPage


def test_inventory_page_loads(logged_in_page):
    """After login, inventory page should load with title 'Products'."""
    inventory = InventoryPage(logged_in_page)

    assert inventory.is_on_inventory_page(), \
        "Not on inventory page after login"
    assert inventory.get_page_title() == "Products", \
        f"Expected title 'Products' but got '{inventory.get_page_title()}'"


def test_inventory_shows_six_products(logged_in_page):
    """Inventory page should display exactly 6 products."""
    inventory = InventoryPage(logged_in_page)

    count = inventory.get_product_count()
    assert count == 6, \
        f"Expected 6 products but found {count}"


def test_all_products_have_name_price_button(logged_in_page):
    """Every product card must have a name, price and Add to Cart button."""
    inventory = InventoryPage(logged_in_page)

    assert inventory.all_products_have_name_price_button(), \
        "One or more products are missing name, price or Add to Cart button"


def test_sort_by_name_a_to_z(logged_in_page):
    """Sorting A→Z should make product names appear in alphabetical order."""
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("az")
    names = inventory.get_all_product_names()

    assert names == sorted(names), \
        f"Products not sorted A→Z. Got: {names}"


def test_sort_by_price_low_to_high(logged_in_page):
    """Sorting low→high should make prices appear in ascending order."""
    inventory = InventoryPage(logged_in_page)

    inventory.sort_by("lohi")
    prices = inventory.get_all_product_prices()

    assert prices == sorted(prices), \
        f"Prices not sorted low→high. Got: {prices}"


def test_add_to_cart_updates_badge(logged_in_page):
    """Adding a product to cart should show badge count of 1."""
    inventory = InventoryPage(logged_in_page)

    # Cart should start empty
    assert inventory.get_cart_count() == 0, \
        "Cart badge should be 0 before adding any product"

    inventory.add_first_product_to_cart()

    # Cart should now show 1
    assert inventory.get_cart_count() == 1, \
        f"Expected cart count 1 but got {inventory.get_cart_count()}"