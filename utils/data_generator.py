from faker import Faker

fake = Faker()


def generate_user_payload():
    return {
        "email": fake.email(),
        "username": fake.user_name(),
        "password": fake.password(),
        "name": {
            "firstname": fake.first_name(),
            "lastname": fake.last_name()
        },
        "address": {
            "city": fake.city(),
            "street": fake.street_name(),
            "number": fake.random_int(min=1, max=9999),
            "zipcode": fake.zipcode(),
            "geolocation": {
                "lat": str(fake.latitude()),
                "long": str(fake.longitude())
            }
        },
        "phone": fake.phone_number()

    }
