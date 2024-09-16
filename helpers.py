import allure
import random
import string
from data import URL_CUSTOMER, URL_CUSTOMER_REG, URL_CUSTOMER_LOGIN
import requests



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

@allure.step('Регистрация курьера')
def customer_registration():
    payload = generate_data_customer()
    response_customer_registration = requests.post(URL_CUSTOMER_REG, data=payload)
    return response_customer_registration, payload

@allure.step('Авторизация курьера')
def customer_authorization(new_customer, payload):
    access_token = new_customer.json()['accessToken']
    response_customer_authorization = requests.post(URL_CUSTOMER_LOGIN, data=payload,
                                           headers={'Authorization': access_token})
    return response_customer_authorization, payload


@allure.step('Удаление курьера')
def delete_customer(registered_customer, payload):
    access_token = registered_customer[0].json()['accessToken']
    response_delete = requests.delete(URL_CUSTOMER, data=payload,
                                           headers={'Authorization': access_token})
    return response_delete
