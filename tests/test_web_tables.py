from pages.web_tables_page import WebTablesPage
from utils.data_generator import generate_user_data

def test_case_2_create_new_user(page):
    web_tables_page = WebTablesPage(page)
    user_data = generate_user_data()

    web_tables_page.open()
    web_tables_page.click_add_user()
    web_tables_page.fill_user_form(user_data)
    assert web_tables_page.is_user_in_table(user_data["email"]), "El usuario no fue creado exitosamente en la tabla"