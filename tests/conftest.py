import pytest
from playwright.sync_api import sync_playwright
import logging
from datetime import datetime
import os

# logging setup...
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=f"{log_dir}/test_log_{datetime.now().strftime('%y%m%d_%H%M%S')}.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# SauceDemo fixture
# ----------------------------
@pytest.fixture(scope="function")
def saucedemo_page():
    logging.info("Launching browser for SauceDemo")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        logging.info("Navigating to SauceDemo website")
        page.goto("https://www.saucedemo.com/")
        yield page
        logging.info("Closing browser")
        context.close()
        browser.close()


