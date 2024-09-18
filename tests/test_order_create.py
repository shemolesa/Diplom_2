import requests
import pytest
import allure
from helpers import generate_ingredient
from data import GET_ORDERS_MESSAGE_401, MENU_BUNS, MENU_SAUCES, MENU_FILLINGS, URL_ORDERS, CREATE_ORDER_MESSAGE_400


class TestOrder:

    @allure.title('Проверка успешного создания заказа без авторизации(только булка, булка с начинкой, '
                  'булка с начинкой и соусом)')
    @pytest.mark.parametrize('ingredients_order', [[generate_ingredient(MENU_BUNS)],
                                                   [generate_ingredient(MENU_BUNS), generate_ingredient(MENU_FILLINGS)],
                                                   [generate_ingredient(MENU_BUNS), generate_ingredient(MENU_FILLINGS), generate_ingredient(MENU_SAUCES)]])
    def test_create_order_unauthorized_ingredients_successfully(self, ingredients_order):
        payload = {"ingredients": ingredients_order} # формируем данные
        # создаем заказ и сохраняем ответ в переменную
        response_create = requests.post(URL_ORDERS, data=payload)
        # проверяем, что заказ создан: возвращаются требуемые статус и результат
        assert response_create.status_code == 200 and response_create.json()['success'] == True

    @allure.title('Проверка невозможности без авторизации создать заказ без ингредиентов')
    def test_create_order_unauthorized_without_ingredients_error(self):
        payload = {} #объявляем переменную с пустым словарем
        # создаем заказ и сохраняем ответ в переменную
        response_create = requests.post(URL_ORDERS, data=payload) # создаем заказ
         # проверяем, что заказ не создан: возвращаются требуемые статус и сообщение
        assert response_create.status_code == 400 and response_create.json()['message'] == CREATE_ORDER_MESSAGE_400

    @allure.title('Проверка невозможности без авторизации создать заказ с неверным хэшем ингредиента(с неверным хэшем,'
                  'с неверным и верным хэшами)')
    @pytest.mark.parametrize('ingredients_order', [["invalidhash"], ["61c0c5a71d1f82001bdaaa6d","invalidhash"]])
    def test_create_order_without_authorzied_invalid_ingredient_error(self, ingredients_order):
        payload = {"ingredients": ingredients_order}# формируем данные
        # создаем заказ и сохраняем ответ в переменную
        response_create = requests.post(URL_ORDERS, data=payload) # создаем заказ
        # проверяем, что заказ не создан: возвращаются требуемые статус и сообщение
        assert response_create.status_code == 500 and 'Internal Server Error' in response_create.text

    @allure.title('Проверка успешного создания заказа c авторизацией(только булка, булка с начинкой, '
                  'булка с начинкой и соусом)')
    @pytest.mark.parametrize('ingredients_order', [[generate_ingredient(MENU_BUNS )],
                                                   [generate_ingredient(MENU_BUNS),generate_ingredient(MENU_FILLINGS)],
                                                   [generate_ingredient(MENU_BUNS),generate_ingredient(MENU_FILLINGS),
                                                    generate_ingredient(MENU_SAUCES)]])
    def test_create_order_authorized_with_ingredients_successfully(self, ingredients_order, response_customer):
        payload = {"ingredients": ingredients_order} # формируем данные
        # создаем заказ и сохраняем ответ в переменную
        response_create = requests.post(URL_ORDERS, data=payload, headers={'Authorization': response_customer[1]})
        # проверяем, что заказ создан: возвращаются требуемые статус и результат
        assert response_create.status_code == 200 and response_create.json()['success'] == True

    @allure.title('Проверка невозможности с авторизацией создать заказ без ингредиентов')
    def test_create_order_authorized_without_ingredients_error(self, response_customer):
        payload = {} # объявляем переменную с пустым словарем
        # создаем заказ и сохраняем ответ в переменную
        response_create = requests.post(URL_ORDERS, data=payload, headers={'Authorization': response_customer[1]})
        # проверяем, что заказ не создан: возвращаются требуемые статус и сообщение
        assert response_create.status_code == 400 and response_create.json()['message'] == CREATE_ORDER_MESSAGE_400

    @allure.title('Проверка невозможности с авторизацией создать заказ с неверным хэшем ингредиента'
                  '(с неверным хэшем,с неверным и верным хэшами)')
    @pytest.mark.parametrize('ingredients_order', [["invalidhash"], ["61c0c5a71d1f82001bdaaa6d","invalidhash"]])
    def test_create_order_authorized_invalid_ingredient_error(self, ingredients_order, response_customer):
        payload = {"ingredients": ingredients_order}# формируем данные
        # создаем заказ и сохраняем ответ в переменную
        response_create = requests.post(URL_ORDERS, data=payload, headers={'Authorization': response_customer[1]})
        # проверяем, что заказ не создан: возвращаются требуемые статус и сообщение
        assert response_create.status_code == 500 and 'Internal Server Error' in response_create.text

    @allure.title('Проверка получения заказов авторизованного покупателя')
    def test_getting_orders_authorized_successfully(self, response_customer):
        # отправляем запрос и сохраняем ответ в переменную
        response_get_orders = requests.get(URL_ORDERS, headers={'Authorization': response_customer[1]})
        # проверяем, что заказ не создан: возвращаются требуемые статус и сообщение
        assert response_get_orders.status_code == 200 and response_get_orders.json()['success'] == True

    @allure.title('Проверка получения заказов без авторизации')
    def test_getting_orders_unauthorized_error(self):
        # отправляем запрос и сохраняем ответ в переменную
        response_get_orders1 = requests.get(URL_ORDERS)
        # проверяем, что заказ не создан: возвращаются требуемые статус и сообщение
        assert (response_get_orders1.status_code == 401 and response_get_orders1.json()['message'] ==
                GET_ORDERS_MESSAGE_401)
