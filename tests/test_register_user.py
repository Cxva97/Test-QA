from pages.register_page import RegisterPage
from utils.data_generator import generate_user_data

def test_case_2_create_new_user(page):
    register_page = RegisterPage(page)
    user_data = generate_user_data()
    
    register_page.open()

    register_page.fill_registration_form(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        username=user_data["username"],
        password=user_data["password"]
    )

    assert register_page.is_form_filled(user_data["username"]), "El formulario de registro no se completó correctamente"