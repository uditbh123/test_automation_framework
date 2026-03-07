import pytest
import logging
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.screenshot import take_screenshot

# ----------------------------
# Session-scoped logging setup
# ----------------------------
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
        filename=f"{log_dir}/test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Test session started")
    yield
    logging.info("Test session ended")

# ----------------------------
# SauceDemo fixture
# ----------------------------
@pytest.fixture(scope="function")
def saucedemo_page():
    headless = os.getenv("CI", "false").lower() == "true"  # headless in CI, headed locally
    logging.info("Launching browser for SauceDemo")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        logging.info("Navigated to SauceDemo")
        yield page
        context.close()
        browser.close()

# ----------------------------
# Screenshot on failure hook
# ----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("saucedemo_page")
        if page:
            screenshot_name = f"FAIL_{item.name}_{datetime.now().strftime('%H%M%S')}"
            path = take_screenshot(page, screenshot_name)
            logging.error(f"Test failed. Screenshot saved: {path}")


@pytest.fixture(scope="function")
def logged_in_page(saucedemo_page):
    """
    Builds on top of saucedemo_page.
    logs in as standard_user and return the page
    already on the inventory screen
    """
    from pages.login_page import LoginPage
    login_page = LoginPage(saucedemo_page)
    login_page.login("standard_user", "secret_sauce")
    saucedemo_page.wait_for_url("**/inventory.html", timeout=5000)
    logging.info("Logged in successfully")
    yield saucedemo_page