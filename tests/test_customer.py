import requests
import pytest
from helpers import generate_data_customer, generate_email, generate_string
from data import URL_CUSTOMER_LOGIN, URL_CUSTOMER, URL_CUSTOMER_REG, CHANGE_MESSAGE_403, CHANGE_MESSAGE_UNREGISTERED_401
import allure


class TestCustomer:


    @allure.title('проверка изменение имэйла и имени авторизованного покупателя')
    @pytest.mark.parametrize('name_data, new_data', [['email', {'email': generate_email()}],
                                                     ['name', {'name': generate_string(8)}]])
    def test_changing_authorized_customer_data_successfully(self, name_data, new_data, response_customer):
        # меняем данные покупателя
        response_ch = requests.patch(URL_CUSTOMER,
                                     headers={'Authorization': response_customer[1]}, json=new_data)
        assert response_ch.status_code == 200 and response_ch.json()['user'][name_data] == new_data[name_data]

    @allure.title('проверка изменение имэйла и имени неавторизованного покупателя')
    @pytest.mark.parametrize('name_data, new_data', [['email', {'email': generate_email()}],
                                                     ['name', {'name': generate_string(8)}]])
    def test_changing_unauthorized_customer_data_successfully(self, name_data, new_data, response_customer_unauthorized):
        # меняем данные покупателя
        response_ch = requests.patch(URL_CUSTOMER,
                                     headers={'Authorization': response_customer_unauthorized[1]}, json=new_data)
        assert response_ch.status_code == 200 and response_ch.json()['user'][name_data] == new_data[name_data]

    @allure.title('проверка изменения пароля авторизованного/неавторизованного покупателя')
    @pytest.mark.parametrize('response', ['response_customer', 'response_customer_unauthorized'])
    def test_changing_customer_password_successfully(self, response, request):
        response_fixture = request.getfixturevalue(response)  # преобразовываем фикстуру
        new_data = {'password': generate_string(8)} # формируем новый пароль
        # меняем данные покупателя
        response_changing = requests.patch(URL_CUSTOMER,
                                           headers={'Authorization': response_fixture[1]}, json=new_data)
        payload = response_fixture[2] # сохраняем исходные данные покупателя из фикстуры
        payload['password'] = new_data['password'] # заменяем пароль в исходных данных
        # авторизуемся с новым паролем
        response_authorization = requests.post(URL_CUSTOMER_LOGIN,
                                               headers={'Authorization': response_fixture[1]}, data=payload)
        # проверяем, что замена выполнилась успешно и пользователь с новым паролем может авторизоваться
        assert ((response_changing.status_code == 200 and response_changing.json()['user']['name'] == payload['name']
                 and response_changing.json()['user']['email'] == payload['email'])
                and
                (response_authorization.status_code == 200 and
                 response_authorization.json()['user']['name'] == payload['name']
                 and response_authorization.json()['user']['email'] == payload['email']))


    @allure.title('проверка одновременного изменения всех данных авторизованного/неавторизованного покупателя')
    @pytest.mark.parametrize('response', ['response_customer', 'response_customer_unauthorized'])
    def test_changing_customer_data_successfully(self, response, request):
        response_fixture = request.getfixturevalue(response) # преобразовываем фикстуру
        new_data = generate_data_customer() # генерируем новые данные покупателя
        # меняем данные покупателя
        response_changing = requests.patch(URL_CUSTOMER,
                                           headers={'Authorization': response_fixture[1]}, json=new_data)
        # регистрируем покупателя с новыми данными
        response_authorization = requests.post(URL_CUSTOMER_LOGIN,
                                               headers={'Authorization': response_fixture[1]}, data=new_data)
        # проверяем, что замена данных прошла успешно и покупатель может зарегистироваться
        assert ((response_changing.status_code == 200 and response_changing.json()['user']['name'] == new_data['name']
                 and response_changing.json()['user']['email'] == new_data['email'])
                and
                (response_authorization.status_code == 200 and
                 response_authorization.json()['user']['name'] == new_data['name']
                 and response_authorization.json()['user']['email'] == new_data['email']))

    @allure.title('проверка невозможности изменения почты, на уже используемvю у авторизованного/'
                  'неавторизованного покупателя')
    @pytest.mark.parametrize('response', ['response_customer', 'response_customer_unauthorized'])
    def test_changing_customer_data_error_403(self, response, request):
        response_fixture = request.getfixturevalue(response) # преобразовываем фикстуру
        another_customer = generate_data_customer() # генерируем  данные нового покупателя
        response_registration = requests.post(URL_CUSTOMER_REG, data=another_customer) # регистрируем нового покупателя
        # сохраняем емайл нового пользователя для замены у тестового покупателя
        new_email = {'email': another_customer['email']}
        # меняем пароль у тестового покупателя
        response_changing = requests.patch(URL_CUSTOMER, headers={'Authorization': response_fixture[1]}, json=new_email)
        # удаляем нового покупателя
        requests.delete(URL_CUSTOMER, headers={'Authorization': response_registration.json()['accessToken']})
        # проверяем, что замена не выполнилась
        assert response_changing.status_code == 403 and response_changing.json()['message'] == CHANGE_MESSAGE_403

    @allure.title('проверка невозможности изменения данных без регистрации пользователя')
    @pytest.mark.parametrize('new_data', [{'email': generate_email()}, {'name': generate_string(8)},
                                          {'password': generate_string(8)}, {'email': generate_email()},
                                          {'name': generate_string(8), 'password': generate_string(8)}])
    def test_changing_unregistered_customer_data_error_401(self, new_data):
        # меняем данные
        response_ch = requests.patch(URL_CUSTOMER, json=new_data)
        assert response_ch.status_code == 401 and response_ch.json()['message'] == CHANGE_MESSAGE_UNREGISTERED_401

