from pages.base_page import BasePage

class SelectMenuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://demoqa.com/select-menu"
        
        # Locators
        self.select_value_input = "#withOptGroup input"
        self.select_one_input = "#selectOne input"
        self.old_style_select = "#oldSelectMenu"
        self.standard_multi_select = "#cars"

    def open(self):
        self.navigate_to(self.url)

    def select_options(self):
        self.page.fill(self.select_value_input, "A root option")
        self.page.keyboard.press("Enter")
        self.page.fill(self.select_one_input, "Ms.")
        self.page.keyboard.press("Enter")
        self.page.select_option(self.old_style_select, label="Indigo")

        multiselect = self.page.locator("#selectMenuContainer").locator("input").nth(2)
        for color in ["Blue", "Red"]:
            multiselect.fill(color)
            self.page.keyboard.press("Enter")
        
        self.page.keyboard.press("Escape")
        self.page.select_option(self.standard_multi_select, label=["Volvo", "Opel"])

    def verify_selections(self) -> bool:
        has_root = self.page.locator("#withOptGroup").get_by_text("A root option").is_visible()
        has_ms = self.page.locator("#selectOne").get_by_text("Ms.").is_visible()

        multi_values = self.page.locator("#selectMenuContainer div[class*='multiValue']")
        has_blue = multi_values.filter(has_text="Blue").count() > 0
        has_red = multi_values.filter(has_text="Red").count() > 0

        cars_locator = self.page.locator(self.standard_multi_select)
        volvo_selected = cars_locator.locator("option[value='volvo']").evaluate("el => el.selected")
        opel_selected = cars_locator.locator("option[value='opel']").evaluate("el => el.selected")

        return has_root and has_ms and has_blue and has_red and volvo_selected and opel_selected