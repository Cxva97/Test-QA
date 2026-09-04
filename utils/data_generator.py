from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "first name": fake.first_name(),
        "last name": fake.last_name(),
        "email": fake.email(),
        "mobile" : fake.phone_number()[:10],
        "address": fake.address().replace("\n", " ")
    }