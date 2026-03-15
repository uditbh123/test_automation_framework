from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class CheckoutPage:
    """
    Page Object Model for the SauceDemo Checkout Flow.
    Handles all 3 steps of the checkout process:
      - Step 1: /checkout-step-one.html   (enter information)
      - Step 2: /checkout-step-two.html   (order summary)
      - Step 3: /checkout-complete.html   (order confirmation)
    """

    def __init__(self, page: Page):
        self.page = page

        # --- Step 1 Locators ---
        self.first_name_input  = page.locator("#first-name")
        self.last_name_input   = page.locator("#last-name")
        self.zip_code_input    = page.locator("#postal-code")
        self.continue_button   = page.locator("#continue")
        self.cancel_button     = page.locator("#cancel")
        self.error_message     = page.locator("[data-test='error']")

        # --- Step 2 Locators ---
        self.finish_button         = page.locator("#finish")
        self.summary_item_names    = page.locator(".inventory_item_name")
        self.summary_item_total    = page.locator(".summary_subtotal_label")
        self.summary_tax           = page.locator(".summary_tax_label")
        self.summary_total         = page.locator(".summary_total_label")

        # --- Step 3 Locators ---
        self.confirmation_header   = page.locator(".complete-header")
        self.back_home_button      = page.locator("#back-to-products")

    
    # Step 1 — Verification
    

    def is_on_step_one(self) -> bool:
        return "checkout-step-one" in self.page.url

    def get_page_title(self) -> str:
        return self.page.locator(".title").text_content().strip()

    def get_error_message(self) -> str:
        try:
            self.error_message.wait_for(state="visible", timeout=2000)
            return self.error_message.text_content().strip()
        except PlaywrightTimeoutError:
            return ""

    
    # Step 1 — Actions
    

    def enter_information(self, first_name: str, last_name: str, zip_code: str) -> None:
        """Fills in the checkout information form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)

    def click_continue(self) -> None:
        self.continue_button.click()

    def click_cancel(self) -> None:
        self.cancel_button.click()


    # Step 2 — Verification
    

    def is_on_step_two(self) -> bool:
        return "checkout-step-two" in self.page.url

    def get_summary_item_names(self) -> list:
        return [
            self.summary_item_names.nth(i).text_content().strip()
            for i in range(self.summary_item_names.count())
        ]

    def get_item_total(self) -> float:
        """Returns item total as float. Text looks like 'Item total: $29.99'"""
        text = self.summary_item_total.text_content().strip()
        return float(text.split("$")[1])

    def get_tax(self) -> float:
        """Returns tax as float. Text looks like 'Tax: $2.40'"""
        text = self.summary_tax.text_content().strip()
        return float(text.split("$")[1])

    def get_total(self) -> float:
        """Returns final total as float. Text looks like 'Total: $32.39'"""
        text = self.summary_total.text_content().strip()
        return float(text.split("$")[1])

    
    # Step 2 — Actions
    

    def click_finish(self) -> None:
        self.finish_button.click()

    
    # Step 3 — Verification
    

    def is_on_confirmation_page(self) -> bool:
        return "checkout-complete" in self.page.url

    def get_confirmation_message(self) -> str:
        try:
            self.confirmation_header.wait_for(state="visible", timeout=3000)
            return self.confirmation_header.text_content().strip()
        except PlaywrightTimeoutError:
            return ""