import requests
import pytest
import allure
from helpers import generate_data_customer
from data import URL_CUSTOMER, URL_CUSTOMER_REG, URL_CUSTOMER_LOGIN

@allure.step('Регистрация нового тестового покупателя и последующее удаление')
@pytest.fixture()
def response_customer_unauthorized():
    # генерируем данные тестового покупателя
    payload = generate_data_customer()
    # отправляем запрос на регистрацию тестового покупателя и сохраняем ответ в переменную
    response_customer_unauthorized = requests.post(URL_CUSTOMER_REG, data=payload)
    # сохраняем токен зарегистрированного покупателя в переменную
    access_token = response_customer_unauthorized.json()['accessToken']
    yield response_customer_unauthorized, access_token, payload
     #удаляем тестового покупателя
    requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})

@allure.step('Регистрация нового тестового покупателя, авторизация и последующее удаление')
@pytest.fixture()
def response_customer(response_customer_unauthorized):
    response_authorization = requests.post(URL_CUSTOMER_LOGIN, data=response_customer_unauthorized[2])
    access_token = response_authorization.json()['accessToken']
    return response_customer_unauthorized[0], access_token, response_customer_unauthorized[2]
