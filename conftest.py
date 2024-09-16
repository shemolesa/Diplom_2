import requests
import pytest
import allure
from helpers import generate_data_customer
from data import URL_CUSTOMER, URL_CUSTOMER_REG, URL_CUSTOMER_LOGIN


@allure.step('Регистрация нового тестового покупателя, авторизация и последующее удаление')
@pytest.fixture()
def response_customer():
    # отправляем запрос на регистрацию тестового покупателя и сохраняем ответ в переменную
    payload = generate_data_customer()
    # отправляем запрос на регистрацию тестового покупателя и сохраняем ответ в переменную
    response_customer = requests.post(URL_CUSTOMER_REG, data=payload)
    # отправляем запрос на авторизацию тестового покупателя и сохраняем ответ в переменную
    response_authorization = requests.post(URL_CUSTOMER_LOGIN, data=payload)
    access_token = response_authorization.json()['accessToken']
#    return response_customer_registration, access_token
    yield response_customer, access_token, payload
     #удаляем тестового покупателя
    response_delete = requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})

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
    response_delete = requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})


# @allure.step('Регистрация нового тестового покупателя с передачей его id и с последующим удалением')
# @pytest.fixture()
# def response_courier():
#     # отправляем запрос на регистрацию тестового курьера и сохраняем ответ в переменную
#     response_courier = requests.post(data.URL_COURIER, data.TEST_COURIER)
#     # отправляем запрос на авторизацию тестового курьера и сохраняем ответ в переменную
#     response_id_courier = requests.post(data.URL_COURIER_LOGIN, data.TEST_COURIER)
#     # находим id курьера
#     id_courier = response_id_courier.json()['id']
#     yield response_courier, response_id_courier
#     #удаляем тестового курьера
#     response_delete = requests.delete(f'{data.URL_COURIER}/{id_courier}')

