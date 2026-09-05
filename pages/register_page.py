from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/register"
        
        # Locators
        self.first_name_input = "#firstname"
        self.last_name_input = "#lastname"
        self.username_input = "#userName"
        self.password_input = "#password"
        self.register_button = "#register"

    def open(self):
        self.navigate_to(self.url)

    def fill_registration_form(self, first_name: str, last_name: str, username: str, password: str):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)

    def click_register(self):
        self.page.click(self.register_button)

    def is_form_filled(self, username: str) -> bool:
        return self.page.locator(self.username_input).input_value() == username