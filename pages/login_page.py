# We are importing Page class from Playwright
# This represents a browser tab
from playwright.sync_api import Page


# This class represents the LOGIN PAGE of the website
# Think of this as a robot which knows how to interact with login screen
class LoginPage:

    # This method runs automatically when object is created
    # It connects our robot with the actual browser page
    def __init__(self, page: Page):

        # Store the browser page inside this class
        self.page = page

        # These are LOCATORS
        # Locator means: "Where is this thing on the webpage?"

        # Username input field location
        self.username_input = "#user-name"

        # Password input field location
        self.password_input = "#password"

        # Login button location
        self.login_button = "#login-button"


    # This function types username in username box
    def enter_username(self, username):

        # Fill username input field
        self.page.fill(self.username_input, username)


    # This function types password in password box
    def enter_password(self, password):

        # Fill password input field
        self.page.fill(self.password_input, password)


    # This function clicks login button
    def click_login(self):

        # Click login button
        self.page.click(self.login_button)


    # This is a COMBINED function
    # Instead of doing all steps separately,
    # we create one function to perform full login action
    def login(self, username, password):

        # Enter username
        self.enter_username(username)

        # Enter password
        self.enter_password(password)

        # Click login button
        self.click_login()