import os

def take_screenshot(page, name):
    screenshots_dir = "reports/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    path = f"{screenshots_dir}/{name}.png"
    page.screenshot(path=path)
    return path