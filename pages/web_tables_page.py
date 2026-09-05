from pages.base_page import BasePage
from playwright.sync_api import expect

class WebTablesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/webtables"
        
        # Locadores
        self.add_button = "#addNewRecordButton"
        self.first_name_input = "#firstName"
        self.last_name_input = "#lastName"
        self.email_input = "#userEmail"
        self.age_input = "#age"
        self.salary_input = "#salary"
        self.department_input = "#department"
        self.submit_button = "#submit"
        self.search_box = "#searchBox"
        self.table_body = ".rt-tbody"

    def open(self):
        self.navigate_to(self.url)
        

    def click_add_user(self):
        self.page.click(self.add_button)

    def fill_user_form(self, user_data: dict):
        self.page.fill(self.first_name_input, user_data["first_name"])
        self.page.fill(self.last_name_input, user_data["last_name"])
        self.page.fill(self.email_input, user_data["email"])
        self.page.fill(self.age_input, str(user_data["age"]))
        self.page.fill(self.salary_input, str(user_data["salary"]))
        self.page.fill(self.department_input, user_data["department"])
        self.page.click(self.submit_button)
        self.page.wait_for_selector("#registration-form-modal", state="hidden", timeout=5000)
        

    def search_user(self, text: str):
        self.page.fill(self.search_box, text)  # un solo fill, sin limpiar antes

    def edit_first_name(self, email: str, new_first_name: str):
        self.search_user(email)
        self.page.locator("span[title='Edit']").click()
        self.page.fill(self.first_name_input, "")
        self.page.fill(self.first_name_input, new_first_name)
        self.page.click(self.submit_button)

    def delete_user(self, email: str):
        self.search_user(email)
        self.page.locator("span[title='Delete']").click()

    def is_user_in_table(self, text: str) -> bool:
        self.search_user(text)
        cell = self.page.get_by_role("cell", name=text, exact=True)
        try:
            expect(cell.first).to_be_visible(timeout=8000)
            return True
        except Exception as e:
            return False