from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class CartPage:
    """
    Page object model for the saucedemo cart page.
    handles all interactions on the cart page.
    """

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.page_title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.cart_item_names = page.locator(".inventory_item_name")
        self.cart_item_prices = page.locator(".inventory_item_price")
        self.remove_buttons = page.locator("button[id^='remove']")
        self.continue_shopping = page.locator("#continue-shopping")
        self.checkout_button = page.locator("#checkout")
        self.cart_badge = page.locator(".shopping_cart_badge")

        # Verification Methods

        def is_on_cart_page(self) -> bool:
            """Confirms we are on the cart page."""
            return (
                "cart" in self.page.url and 
                self.page_title.is_visible()
            )
        
        def get_page_title(self) -> str:
            return self.page_title.text_content().strip()
        
        def get_cart_item_count(self) -> int:
            """Returns number of items currently in the cart."""
            return self.cart_items.count()
        
        def get_cart_item_names(self) -> list:
            """Returns list of all product name strings in cart."""
            return [
                self.cart_item_names.nth(i).text_content().strip()
                for i in range(self.cart_item_names.count())
            ]
        
        def get_cart_item_prices(self) -> list:
            """Returns list of product prices as floats in cart."""
            prices = []
            for i in range(self.cart_item_prices.count()):
                price_text = self.cart_item_prices.nth(i).text_content().strip()
                prices.append(float(price_text.replace("$", "")))

        def is_cart_empty(self) -> bool:
            """Returns True if no items are in the cart."""
            return self.cart_items.count() == 0
        
        def is_cart_badge_visible(self) -> bool:
            """Returns True if cart badge is visible."""
            return self.cart_badge.is_visible()
        
        # Action Methods

        def remove_first_item(self) -> None:
            """Clicks Remove on the first cart item."""
            self.remove_buttons.first.click()

        def click_continue_shopping(self) -> None:
            """Clicks Continue Shopping button."""
            self.continue_shopping.click()

        def click_checkout(self) -> None:
            """Clicks checkout button."""
            self.checkout_button.click()