import os
from pages.practice_form_page import PracticeFormPage
from utils.data_generator import generate_user_data

def test_fill_practice_form(page, tmp_path):
    form_page = PracticeFormPage(page)
    user_data = generate_user_data()
    
    image_path = os.path.join(tmp_path , "test_image.png")
    with open(image_path, "wb") as f:
        f.write(b"fake image content")
        
    form_page.open()
    form_page.fill_form(user_data, file_path=image_path)
    form_page.submit()
    assert form_page.is_submission_successful(), "El formulario no se envió correctamente"