from generators import *


class Credentials:
    @staticmethod
    def generate_user_data(email=True, password=True, name=True):
        data = {}
        if email:
            data["email"] = generate_user_email()
        if password:
            data["password"] = generate_user_password()
        if name:
            data["name"] = generate_user_username()
        return data

class DataIngredients:
    data_ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]