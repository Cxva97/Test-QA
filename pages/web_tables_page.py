from pages.base_page import BasePage

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

    def is_user_in_table(self, email: str) -> bool:
        self.page.fill(self.search_box, email)
        return self.page.is_visible(f"text={email}")