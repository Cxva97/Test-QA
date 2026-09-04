from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/automation-practice-form"
        
        # Locadores
        self.first_name_input = "#firstName"
        self.last_name_input = "#lastName"
        self.user_email_input = "#userEmail"
        self.gender_male_radio = "label[for='gender-radio-1']"
        self.user_number_input = "#userNumber"
        self.hobbies_sports_checkbox = "label[for='hobbies-checkbox-1']"
        self.current_address_input = "#currentAddress"
        self.submit_button = "#submit"
        self.modal_title = "#example-modal-sizes-title-lg"

    def open(self):
        self.navigate_to(self.url)

    def fill_form(self, data: dict):
        self.page.fill(self.first_name_input, data["first_name"])
        self.page.fill(self.last_name_input, data["last_name"])
        self.page.fill(self.user_email_input, data["email"])
        self.page.click(self.gender_male_radio)
        self.page.fill(self.user_number_input, data["mobile"])
        self.page.click(self.hobbies_sports_checkbox)
        self.page.fill(self.current_address_input, data["address"])

    def submit(self):
        self.remove_ads()
        self.page.click(self.submit_button)

    def is_submission_successful(self) -> bool:
        return self.page.is_visible(self.modal_title)