import pytest 
from playwright.sync_api import sync_playwright
import logging
from datetime import datetime 
import os

# Setup logging 
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=f"{log_dir}/test_log_{datetime.now().strftime('%y%m%d_%H%M%S')}.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Browser Fixture 
@pytest.fixture(scope="function")
def page():
    logging.info("Launching browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        logging.info("Closing browser")
        browser.close()
