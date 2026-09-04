from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/automation-practice-form"
        
        # Locators
        self.first_name_input = "#firstName"
        self.last_name_input = "#lastName"
        self.user_email_input = "#userEmail"
        self.gender_male_radio = "label[for='gender-radio-1']"
        self.user_number_input = "#userNumber"
        self.date_of_birth_input = "#dateOfBirthInput"
        self.subjects_input = "#subjectsInput"
        self.hobbies_sports_checkbox = "label[for='hobbies-checkbox-1']"
        self.picture_upload_input = "#uploadPicture"
        self.current_address_input = "#currentAddress"
        self.state_input = "#react-select-3-input"
        self.city_input = "#react-select-4-input"
        self.submit_button = "#submit"
        self.modal_title = "#example-modal-sizes-title-lg"

    def open(self):
        self.navigate_to(self.url)

    def fill_form(self, data: dict, file_path: str = None):
        self.page.fill(self.first_name_input, data["first_name"])
        self.page.fill(self.last_name_input, data["last_name"])
        self.page.fill(self.user_email_input, data["email"])
        self.page.click(self.gender_male_radio)
        self.page.fill(self.user_number_input, data["mobile"])
        self.page.fill(self.subjects_input,"Computer Science")
        self.page.keyboard.press("Enter")
        self.page.click(self.hobbies_sports_checkbox)
        
        if file_path:
            self.page.set_input_files(self.picture_upload_input, file_path)
            
        self.page.fill(self.current_address_input, data["address"])
        self.page.fill(self.state_input, "NCR")
        self.page.keyboard.press("Enter")
        self.page.fill(self.city_input, "Gurgaon")
        self.page.keyboard.press("Enter")

    def submit(self):
        self.remove_ads()
        self.page.locator(self.submit_button).scroll_into_view_if_needed()
        self.page.locator(self.submit_button).click(force=True)

    def is_submission_successful(self) -> bool:
        try:
            self.page.wait_for_selector(self.modal_title, timeout=5000)
            return self.page.is_visible(self.modal_title)
        except Exception:
            return False