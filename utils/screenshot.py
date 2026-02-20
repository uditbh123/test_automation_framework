# This function will take screenshot when test fails

def take_screenshot(page, name):

    # Save screenshot inside reports folder
    # name will be the screenshot file name

    page.screenshot(path=f"reports/{name}.png")