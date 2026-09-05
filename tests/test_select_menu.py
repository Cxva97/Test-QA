from pages.select_menu_page import SelectMenuPage

def test_select_menu(page):
    select_menu_page = SelectMenuPage(page)

    select_menu_page.open()
    select_menu_page.select_options()
    assert select_menu_page.verify_selections(), "No se seleccionaron correctamente las opciones en Select Menu"