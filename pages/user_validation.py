from pages.base_page import BasePage

class UserFormModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.modal_selector = "#registration-form-modal"
        self.first_name_input = "#firstName"
        self.last_name_input = "#lastName"
        self.email_input = "#userEmail"
        self.age_input = "#age"
        self.salary_input = "#salary"
        self.department_input = "#department"
        self.submit_button = "#submit"

    def is_visible(self) -> bool:
        return self.page.locator(self.modal_selector).is_visible()

    def fill_form(self, first_name="", last_name="", email="", age="", salary="", department=""):
        if first_name: self.page.fill(self.first_name_input, first_name)
        if last_name: self.page.fill(self.last_name_input, last_name)
        if email: self.page.fill(self.email_input, email)
        if age: self.page.fill(self.age_input, str(age))
        if salary: self.page.fill(self.salary_input, str(salary))
        if department: self.page.fill(self.department_input, department)

    def submit(self):
        self.page.click(self.submit_button)

    def close(self):
        self.page.get_by_role("button", name="Close").click()