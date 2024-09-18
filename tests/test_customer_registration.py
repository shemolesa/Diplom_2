import requests
import pytest
import allure
from helpers import generate_email, generate_string, generate_data_customer
from data import URL_CUSTOMER_REG, REGISTRATION_MESSAGE_403, REGISTRATION_MESSAGE_NOT_ENOUGH_DATA_403, URL_CUSTOMER


class TestCustomer:

    @allure.title('Проверка успешной регистрации покупателя с полным набором данных')
    def test_registration_customer_complete_data_successfully(self):
        payload = generate_data_customer() #генерируем данные покупателя
        response_registration = requests.post(URL_CUSTOMER_REG, data=payload) # регистрируем тестового покупателя
        access_token = response_registration.json()['accessToken'] # получаем токен зарегистрированного покупателя
        # удаляем тестового покупателя
        requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})
        # проверяем, что покупатель зарегистрирован
        assert response_registration.status_code == 200 and response_registration.json()['success'] == True

    @allure.title('Проверка невозможности регистрации покупателя с повторяющимся логином')
    def test_registration_customer_double_error(self, response_customer_unauthorized):
       # отправляем запрос на регистрацию покупателя с повторяющимся логином и сохраняем ответ в переменную response
        response = requests.post(URL_CUSTOMER_REG, data=response_customer_unauthorized[2])
        # проверяем, что покупатель не зарегистрирован, выдалось соответствующее сообщение
        assert response.status_code == 403 and response.json()['message'] == REGISTRATION_MESSAGE_403

    @allure.title('Проверка невозможности регистрации пользователя с неполными обязательными полями')
    @pytest.mark.parametrize('payload', [{"email": generate_email(), "name": generate_string(6)},
                                         {"password": generate_string(6), "name": generate_string(6)},
                                         {"email": generate_email(), "password": generate_string(6)}])
    def test_registration_customer_incomplete_data_error(self, payload):
        # отправляем запрос на регистрацию покупателя и сохраняем ответ в переменную response
        response = requests.post(URL_CUSTOMER_REG, data=payload)
        # проверяем, что покупателя не зарегистрирован, выдалось соответствующее сообщение
        assert (response.status_code == 403 and response.json()['message'] ==
                REGISTRATION_MESSAGE_NOT_ENOUGH_DATA_403)


