from pages.web_tables_page import WebTablesPage
from utils.data_generator import generate_user_data

def test_create_new_user(page):
    web_tables_page = WebTablesPage(page)
    user_data = generate_user_data()
    updated_name = "UpdateName"

    web_tables_page.open()
    web_tables_page.click_add_user()
    web_tables_page.fill_user_form(user_data)
    assert web_tables_page.is_user_in_table(user_data["email"]), "Error: El usuario no fue creado."

    web_tables_page.edit_first_name(user_data["email"], updated_name)
    assert web_tables_page.is_user_in_table(updated_name), "Error: El usuario no actualizó su nombre."

    web_tables_page.delete_user(user_data["email"])
    assert not web_tables_page.is_user_in_table(updated_name), "Error: El usuario no fue eliminado de la tabla."