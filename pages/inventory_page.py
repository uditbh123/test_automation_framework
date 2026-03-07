from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class InventoryPage:
    """
    Page Object Model for the SauceDemo Inventory Page.
    Handles all interactions on the products listing page.
    """

    def __init__(self, page: Page):
        self.page = page

        # --- Locators ---
        self.page_title        = page.locator(".title")
        self.product_cards     = page.locator(".inventory_item")
        self.product_names     = page.locator(".inventory_item_name")
        self.product_prices    = page.locator(".inventory_item_price")
        self.add_to_cart_buttons = page.locator("button[id^='add-to-cart']")
        self.sort_dropdown     = page.locator(".product_sort_container")
        self.cart_badge        = page.locator(".shopping_cart_badge")

    # Verification Methods
    

    def is_on_inventory_page(self) -> bool:
        """Checks URL and page title to confirm we are on inventory page."""
        return (
            "inventory" in self.page.url and
            self.page_title.is_visible()
        )

    def get_page_title(self) -> str:
        return self.page_title.text_content().strip()

    def get_product_count(self) -> int:
        """Returns total number of product cards visible."""
        return self.product_cards.count()

    def get_all_product_names(self) -> list:
        """Returns list of all product name strings."""
        return [
            self.product_names.nth(i).text_content().strip()
            for i in range(self.product_names.count())
        ]

    def get_all_product_prices(self) -> list:
        """Returns list of product prices as floats."""
        prices = []
        for i in range(self.product_prices.count()):
            # price text looks like "$9.99" — strip the $ and convert
            price_text = self.product_prices.nth(i).text_content().strip()
            prices.append(float(price_text.replace("$", "")))
        return prices

    def all_products_have_name_price_button(self) -> bool:
        """
        Verifies every product card has a name, price and add-to-cart button.
        Returns False if any product is missing any of these.
        """
        count = self.get_product_count()
        for i in range(count):
            card = self.product_cards.nth(i)
            has_name   = card.locator(".inventory_item_name").is_visible()
            has_price  = card.locator(".inventory_item_price").is_visible()
            has_button = card.locator("button").is_visible()
            if not (has_name and has_price and has_button):
                return False
        return True

    
    # Action Methods
    

    def sort_by(self, option: str) -> None:
        """
        Sorts products using the dropdown.
        option values: 'az', 'za', 'lohi', 'hilo'
        """
        self.sort_dropdown.select_option(option)

    def add_first_product_to_cart(self) -> None:
        """Clicks Add to Cart on the first product."""
        self.add_to_cart_buttons.first.click()

    def get_cart_count(self) -> int:
        """
        Returns the cart badge number.
        Returns 0 if badge is not visible (empty cart).
        """
        try:
            self.cart_badge.wait_for(state="visible", timeout=2000)
            return int(self.cart_badge.text_content().strip())
        except PlaywrightTimeoutError:
            return 0