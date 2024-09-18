import allure
import random
import string


@allure.step('Генерация строкового значения')
def generate_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерация email')
def generate_email():
    email_str = generate_string(8)+"@yandex.ru"
    return email_str

@allure.step('Генерация данных курьера для регистрации')
def generate_data_customer():
    customer = {
    "email": generate_email(),
    "password": generate_string(8),
    "name": generate_string(8)
}
    return customer

@allure.step('Генерация ингредиента')
def generate_ingredient(list_ingredients):
    random_ingredients = random.choice(list_ingredients)
    return random_ingredients
