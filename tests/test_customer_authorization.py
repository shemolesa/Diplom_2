import requests
import pytest
import allure
from data import (TEST_CUSTOMER, URL_CUSTOMER_REG, URL_CUSTOMER_LOGIN, URL_CUSTOMER,
                  AUTHORIZATION_MESSAGE_INCORRECT_DATA_401)


class TestCourierAuthorization:

    @allure.title('Проверка успешной авторизации покупателя с реальными данными')
    def test_authorization_customer_real_data_successfully(self, response_customer_unauthorized):
        # авторизуем покупателя
        response_authorization = requests.post(URL_CUSTOMER_LOGIN,
                                               headers={'Authorization': response_customer_unauthorized[1]},
                                               data=response_customer_unauthorized[2])
        # проверяем, что тестовый покупатель залогинился: вернулись код 200 и
        # верные данные авторизованного покупателя
        assert (response_authorization.status_code == 200 and response_authorization.json()['user'] ==
                response_customer_unauthorized[0].json()['user'])


    @allure.title('Проверка авторизации покупателя с некорректным логином/паролем')
    @pytest.mark.parametrize('payload_incorrect', [{"email": TEST_CUSTOMER['email'], "password": 'wrong_password'},
                                                   {"email": 'wrong_email@ya.ru',
                                                    "password": TEST_CUSTOMER['password']}])
    def test_authorization_customer_incomplete_data_error(self, payload_incorrect):
        # регистрируем тестового покупателя
        response_registration = requests.post(URL_CUSTOMER_REG, data=TEST_CUSTOMER)
        # авторизуемся с некорректным логином/паролем
        response_authorization = requests.post(URL_CUSTOMER_LOGIN, data=payload_incorrect)
        # удаляем тестового покупателя
        response_delete = requests.delete(URL_CUSTOMER, data=TEST_CUSTOMER,
                                          headers={'Authorization': response_registration.json()['accessToken']})
        # проверяем, что авторизация не выполнена
        assert response_authorization.status_code == 401 and response_authorization.json()[
            'message'] == AUTHORIZATION_MESSAGE_INCORRECT_DATA_401
