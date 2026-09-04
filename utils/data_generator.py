import random
from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "mobile" : fake.numerify(text="##########"),
        "address": fake.address().replace("\n", " "),
        "age": random.randint(18,63),
        "salary": random.randint(1500,4500),
        "department": fake.job().split()[0]
    }