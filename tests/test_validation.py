from pages.web_tables_page import WebTablesPage
from pages.user_validation import UserFormModal

def test_empty_fields_validation(page):
    web_tables = WebTablesPage(page)
    modal = UserFormModal(page)

    web_tables.open()
    web_tables.click_add_user()
    modal.submit()
    assert modal.is_visible(), "Error: El formulario se envió estando vacío"

def test_invalid_format_validation(page):
    web_tables = WebTablesPage(page)
    modal = UserFormModal(page)

    web_tables.open()
    web_tables.click_add_user()

    modal.fill_form(
        first_name="Cesar",
        last_name="Villacis",
        email="correo invalido",
        age="wer",
        salary="rrttythg",
        department="QA"
    )
    modal.submit()

    assert modal.is_visible(), "Error: El formulario aceptó datos con formato inválido"

    modal.close()
    assert not web_tables.is_user_in_table("correo invalido"), "Error: El registro inválido se guardó en la tabla"